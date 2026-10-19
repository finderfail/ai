from __future__ import annotations

import json
import threading
from pathlib import Path

import requests
from fastapi import Depends, FastAPI, HTTPException, Request, Response
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from rag import config
from rag.draft import generate_draft
from rag.llm import check_ollama_available
from rag.pipeline import answer_stream

from . import accounts, db, geo, i18n, openai_api, sanctions
from .model_queue import closing_stream, model_queue, queued

app = FastAPI(title="Kriloud AI")

STATIC_DIR = Path(__file__).resolve().parent / "static"
PRIVATE_DIR = Path(__file__).resolve().parent / "private"
SESSION_COOKIE = "kriloud_session"
SESSION_MAX_AGE = accounts.SESSION_TTL_DAYS * 86400

_draft_state: dict = {"incoming": None, "draft": None, "sources": []}

db.init_db()


def _warm_up() -> None:
    try:
        from rag.embeddings import embed_query
        from rag.llm import stream_generate
        from rag.pipeline import _get_store

        _get_store()
        embed_query("warm up")
        default_model = config.MODELS[config.DEFAULT_MODEL]["ollama_model"]
        for _ in stream_generate(
            "warm up",
            config.TEMPERATURE,
            model=default_model,
            options={"num_predict": 1},
        ):
            pass
    except Exception:
        pass


threading.Thread(target=_warm_up, daemon=True).start()


@app.middleware("http")
async def no_store_static(request: Request, call_next):
    response = await call_next(request)
    if not request.url.path.startswith("/api/"):
        response.headers["Cache-Control"] = "no-cache, must-revalidate"
    return response


@app.middleware("http")
async def geo_whitelist(request: Request, call_next):
    client_host = request.client.host if request.client else None
    if geo.is_allowed(request.headers, client_host):
        return await call_next(request)
    path = request.url.path
    if path.startswith("/api/") or path.startswith("/v1/"):
        return JSONResponse(
            status_code=451,
            content={"detail": geo.BLOCK_MESSAGE, "error": {"message": geo.BLOCK_MESSAGE, "code": "region_not_supported"}},
        )
    return HTMLResponse(geo.BLOCK_PAGE, status_code=451)


class ChatRequest(BaseModel):
    message: str
    history: list[dict] = []


class AuthRequest(BaseModel):
    email: str
    password: str


class LanguageRequest(BaseModel):
    language: str


class ModelRequest(BaseModel):
    model: str


class KeyRequest(BaseModel):
    name: str = ""


class DraftRequest(BaseModel):
    message: str


def request_language(request: Request) -> str:
    return i18n.resolve(request.headers.get("x-lang"))


def enforce_sanctions(email: str, language: str) -> None:
    block = sanctions.check(email=email)
    if block is not None:
        raise HTTPException(status_code=403, detail=i18n.text(f"sanction.{block.reason}", language))


def current_user(request: Request) -> accounts.User | None:
    user = accounts.user_by_session(request.cookies.get(SESSION_COOKIE))
    if user is not None:
        enforce_sanctions(user.email, user.language)
    return user


def require_user(
    request: Request, user: accounts.User | None = Depends(current_user)
) -> accounts.User:
    if user is None:
        raise HTTPException(
            status_code=401, detail=i18n.text("login_required", request_language(request))
        )
    return user


def user_payload(user: accounts.User) -> dict:
    payload = {
        "authenticated": True,
        "email": user.email,
        "plan": user.plan,
        "plan_label": user.plan_label,
        "language": user.language,
        "quota": accounts.quota_status(user),
    }
    payload["model"] = user.active_model
    payload["models"] = [
        {"id": model_id, "label": config.MODELS[model_id]["label"]}
        for model_id in user.available_models
    ]
    if user.governance:
        payload["modules"] = ["/api/ui/governance.js"]
        payload["governance"] = {"enabled": True}
    return payload


def start_session(response: Response, user: accounts.User) -> None:
    token = accounts.create_session(user.id)
    response.set_cookie(
        SESSION_COOKIE, token, httponly=True, samesite="lax", max_age=SESSION_MAX_AGE
    )


@app.post("/api/auth/register")
def register(payload: AuthRequest, request: Request, response: Response):
    language = request_language(request)
    enforce_sanctions(payload.email, language)
    try:
        user = accounts.register(payload.email, payload.password, language=language)
    except accounts.AccountError as exc:
        raise HTTPException(status_code=400, detail=exc.message(language))
    start_session(response, user)
    return user_payload(user)


@app.post("/api/auth/login")
def login(payload: AuthRequest, request: Request, response: Response):
    language = request_language(request)
    enforce_sanctions(payload.email, language)
    try:
        user = accounts.authenticate(payload.email, payload.password)
    except accounts.AccountError as exc:
        raise HTTPException(status_code=401, detail=exc.message(language))
    start_session(response, user)
    return user_payload(user)


@app.post("/api/auth/logout")
def logout(request: Request, response: Response):
    accounts.delete_session(request.cookies.get(SESSION_COOKIE))
    response.delete_cookie(SESSION_COOKIE)
    return {"ok": True}


@app.get("/api/auth/me")
def me(user: accounts.User | None = Depends(current_user)):
    if user is None:
        return {"authenticated": False}
    return user_payload(user)


@app.get("/api/plans")
def plans():
    return accounts.plans_overview()


@app.get("/api/languages")
def languages():
    return accounts.languages_overview()


@app.put("/api/settings/language")
def put_language(payload: LanguageRequest, user: accounts.User = Depends(require_user)):
    try:
        accounts.set_language(user.id, payload.language)
    except accounts.AccountError as exc:
        raise HTTPException(status_code=400, detail=exc.message(user.language))
    return {"language": payload.language}


@app.put("/api/settings/model")
def put_model(payload: ModelRequest, user: accounts.User = Depends(require_user)):
    try:
        accounts.set_model(user, payload.model)
    except accounts.AccountError as exc:
        raise HTTPException(status_code=400, detail=exc.message(user.language))
    return {"model": payload.model}


@app.get("/api/ui/governance.js")
def governance_module(user: accounts.User | None = Depends(current_user)):
    if user is None or not user.governance:
        raise HTTPException(status_code=404, detail="Not Found")
    return FileResponse(
        PRIVATE_DIR / "governance.js",
        media_type="text/javascript",
        headers={"Cache-Control": "no-store"},
    )


@app.get("/api/keys")
def get_keys(user: accounts.User = Depends(require_user)):
    return accounts.list_access_keys(user.id)


@app.post("/api/keys")
def post_key(payload: KeyRequest, user: accounts.User = Depends(require_user)):
    try:
        return accounts.create_access_key(user.id, payload.name)
    except accounts.AccountError as exc:
        raise HTTPException(status_code=400, detail=exc.message(user.language))


@app.delete("/api/keys/{key_id}")
def delete_key(key_id: int, user: accounts.User = Depends(require_user)):
    try:
        accounts.delete_access_key(user.id, key_id)
    except accounts.AccountError as exc:
        raise HTTPException(status_code=404, detail=exc.message(user.language))
    return {"ok": True}


@app.get("/api/usage")
def usage(user: accounts.User = Depends(require_user)):
    return {"quota": accounts.quota_status(user), "by_day": accounts.usage_by_day(user.id)}


@app.get("/api/health")
def health():
    ok, message = check_ollama_available()
    models = sorted({model["ollama_model"] for model in config.MODELS.values()})
    return {
        "ok": ok,
        "message": message,
        "model": config.MODELS[config.DEFAULT_MODEL]["ollama_model"],
        "models": models,
        "queue": model_queue.stats(),
    }


def sse(payload: dict) -> str:
    return f"data: {json.dumps(payload, ensure_ascii=False)}\n\n"


@app.post("/api/chat")
def chat(req: ChatRequest, user: accounts.User = Depends(require_user)):
    quota = accounts.quota_status(user)
    if quota["exceeded"]:
        raise HTTPException(
            status_code=429,
            detail=i18n.text(
                "quota_exceeded",
                user.language,
                plan=user.plan_label,
                used=quota["used_today"],
                limit=quota["limit"],
            ),
        )

    def event_stream():
        usage_stats: dict = {}
        try:
            _, token_stream = answer_stream(
                req.message,
                usage=usage_stats,
                language=user.language,
                domains=user.rag_domains,
                **config.model_request(user.active_model, req.history),
            )
        except FileNotFoundError as exc:
            yield sse({"type": "error", "text": str(exc)})
            return

        try:
            for kind, value in queued(token_stream):
                if kind == "queue":
                    yield sse({"type": "queue", "position": value})
                elif kind == "start":
                    yield sse({"type": "queue_done"})
                else:
                    yield sse({"type": "token", "text": value})
        except requests.Timeout:
            yield sse({"type": "error", "text": i18n.text("model_timeout", user.language)})
            return
        except requests.RequestException as exc:
            yield sse(
                {"type": "error", "text": i18n.text("model_error", user.language, error=exc)}
            )
            return

        prompt_tokens = usage_stats.get("prompt_tokens", 0)
        completion_tokens = usage_stats.get("completion_tokens", 0)
        accounts.record_usage(user.id, prompt_tokens, completion_tokens)

        yield sse(
            {
                "type": "done",
                "usage": {"prompt_tokens": prompt_tokens, "completion_tokens": completion_tokens},
                "quota": accounts.quota_status(user),
            }
        )

    return closing_stream(event_stream())


@app.post("/api/draft")
def post_draft(payload: DraftRequest):
    draft, sources = generate_draft(payload.message)
    _draft_state.update({"incoming": payload.message, "draft": draft, "sources": sources})
    return _draft_state


@app.get("/api/draft/latest")
def get_draft_latest():
    return _draft_state


@app.get("/draft")
def draft_page():
    return FileResponse(STATIC_DIR / "draft.html")


@app.get("/login")
def login_page():
    return FileResponse(STATIC_DIR / "login.html")


app.include_router(openai_api.router)

app.mount("/", StaticFiles(directory=str(STATIC_DIR), html=True), name="static")
