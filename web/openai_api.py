from __future__ import annotations

import json
import secrets
import time

import requests
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from rag import config
from rag.llm import stream_generate
from rag.pipeline import answer_stream

from . import accounts, i18n, sanctions
from .model_queue import closing_stream, queued

router = APIRouter(prefix="/v1")

AUTOCOMPLETE_TEMPERATURE = 0.2


class ApiError(Exception):
    def __init__(self, status: int, message: str, error_type: str, code: str):
        self.status = status
        self.message = message
        self.error_type = error_type
        self.code = code


def error_response(exc: ApiError) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status,
        content={"error": {"message": exc.message, "type": exc.error_type, "code": exc.code}},
    )


class ChatCompletionRequest(BaseModel):
    model: str | None = None
    messages: list[dict]
    stream: bool = False
    temperature: float | None = None
    top_p: float | None = None
    max_tokens: int | None = None
    max_completion_tokens: int | None = None
    stop: str | list[str] | None = None


class CompletionRequest(BaseModel):
    model: str | None = None
    prompt: str | list[str] = ""
    suffix: str | None = None
    stream: bool = False
    temperature: float | None = None
    top_p: float | None = None
    max_tokens: int | None = None
    stop: str | list[str] | None = None


def authenticate(request: Request) -> accounts.User:
    header = request.headers.get("authorization", "")
    raw_key = header[7:] if header.lower().startswith("bearer ") else request.headers.get("x-api-key")
    user = accounts.user_by_access_key(raw_key)
    if user is None:
        raise ApiError(401, i18n.text("invalid_key"), "invalid_request_error", "invalid_api_key")
    block = sanctions.check(email=user.email)
    if block is not None:
        raise ApiError(
            403,
            i18n.text(f"sanction.{block.reason}", user.language),
            "permission_error",
            "account_blocked",
        )
    quota = accounts.quota_status(user)
    if quota["exceeded"]:
        raise ApiError(
            429,
            i18n.text(
                "quota_exceeded",
                user.language,
                plan=user.plan_label,
                used=quota["used_today"],
                limit=quota["limit"],
            ),
            "insufficient_quota",
            "quota_exceeded",
        )
    return user


def resolve_model(user: accounts.User, requested: str | None) -> str:
    if not requested:
        return user.active_model
    if requested in user.available_models:
        return requested
    raise ApiError(
        404,
        i18n.text("model_not_found", user.language, model=requested),
        "invalid_request_error",
        "model_not_found",
    )


def text_of(content) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for part in content:
            if isinstance(part, dict) and part.get("type") in ("text", "input_text"):
                parts.append(str(part.get("text", "")))
            elif isinstance(part, str):
                parts.append(part)
        return "\n".join(parts)
    return ""


def split_messages(messages: list[dict]) -> tuple[str, list[dict], str]:
    system_parts: list[str] = []
    dialog: list[dict] = []
    for message in messages:
        role = message.get("role")
        content = text_of(message.get("content"))
        if role in ("system", "developer"):
            if content:
                system_parts.append(content)
        elif role in ("user", "assistant") and content:
            dialog.append({"role": role, "content": content})
    question = ""
    if dialog and dialog[-1]["role"] == "user":
        question = dialog.pop()["content"]
    return "\n\n".join(system_parts), dialog, question


def ollama_options(max_tokens: int | None, top_p: float | None, stop) -> dict:
    options: dict = {}
    if max_tokens:
        options["num_predict"] = max_tokens
    if top_p is not None:
        options["top_p"] = top_p
    if stop:
        options["stop"] = [stop] if isinstance(stop, str) else list(stop)
    return options


def chunk_line(payload: dict) -> str:
    return f"data: {json.dumps(payload, ensure_ascii=False)}\n\n"


def run_stream(user, model_id, token_stream, usage, make_chunk, make_final):
    def events():
        try:
            for kind, value in queued(token_stream):
                if kind == "queue":
                    yield f": queue position {value}\n\n"
                elif kind == "token":
                    yield chunk_line(make_chunk(value))
        except requests.RequestException:
            yield chunk_line(
                {
                    "error": {
                        "message": i18n.text("model_timeout", user.language),
                        "type": "server_error",
                    }
                }
            )
            return
        finally:
            accounts.record_usage(
                user.id, usage.get("prompt_tokens", 0), usage.get("completion_tokens", 0)
            )
        yield chunk_line(make_final())
        yield "data: [DONE]\n\n"

    return closing_stream(events())


def finish_reason(usage: dict, max_tokens: int | None) -> str:
    if max_tokens and usage.get("completion_tokens", 0) >= max_tokens:
        return "length"
    return "stop"


def usage_block(usage: dict) -> dict:
    prompt = usage.get("prompt_tokens", 0)
    completion = usage.get("completion_tokens", 0)
    return {"prompt_tokens": prompt, "completion_tokens": completion, "total_tokens": prompt + completion}


def collect(user, token_stream, usage) -> str:
    try:
        return "".join(value for kind, value in queued(token_stream) if kind == "token")
    except requests.RequestException:
        raise ApiError(502, i18n.text("model_timeout", user.language), "server_error", "upstream_error")
    finally:
        accounts.record_usage(
            user.id, usage.get("prompt_tokens", 0), usage.get("completion_tokens", 0)
        )


@router.get("/models")
def list_models(request: Request):
    try:
        user = authenticate(request)
    except ApiError as exc:
        return error_response(exc)
    created = int(time.time())
    return {
        "object": "list",
        "data": [
            {"id": model_id, "object": "model", "created": created, "owned_by": "universal-kriloud"}
            for model_id in user.available_models
        ],
    }


@router.post("/chat/completions")
def chat_completions(req: ChatCompletionRequest, request: Request):
    try:
        user = authenticate(request)
        model_id = resolve_model(user, req.model)
        client_system, history, question = split_messages(req.messages)
        if not question:
            raise ApiError(400, "messages must end with a user message", "invalid_request_error", "invalid_messages")
        usage: dict = {}
        profile = config.model_request(model_id, history)
        options = {**(profile.pop("options") or {}), **ollama_options(req.max_completion_tokens or req.max_tokens, req.top_p, req.stop)}
        style = profile.pop("client_system")
        if req.temperature is not None:
            profile["temperature"] = req.temperature
        _, token_stream = answer_stream(
            question,
            usage=usage,
            language=user.language,
            domains=user.rag_domains,
            client_system="\n\n".join(part for part in (client_system, style) if part) or None,
            options=options or None,
            **profile,
        )
        max_tokens = req.max_completion_tokens or req.max_tokens
        completion_id = f"chatcmpl-{secrets.token_hex(12)}"
        created = int(time.time())

        if req.stream:
            def make_chunk(token: str) -> dict:
                return {
                    "id": completion_id,
                    "object": "chat.completion.chunk",
                    "created": created,
                    "model": model_id,
                    "choices": [{"index": 0, "delta": {"role": "assistant", "content": token}, "finish_reason": None}],
                }

            def make_final() -> dict:
                return {
                    "id": completion_id,
                    "object": "chat.completion.chunk",
                    "created": created,
                    "model": model_id,
                    "choices": [{"index": 0, "delta": {}, "finish_reason": finish_reason(usage, max_tokens)}],
                    "usage": usage_block(usage),
                }

            return run_stream(user, model_id, token_stream, usage, make_chunk, make_final)

        text = collect(user, token_stream, usage)
        return {
            "id": completion_id,
            "object": "chat.completion",
            "created": created,
            "model": model_id,
            "choices": [
                {
                    "index": 0,
                    "message": {"role": "assistant", "content": text},
                    "finish_reason": finish_reason(usage, max_tokens),
                }
            ],
            "usage": usage_block(usage),
        }
    except ApiError as exc:
        return error_response(exc)


@router.post("/completions")
def completions(req: CompletionRequest, request: Request):
    try:
        user = authenticate(request)
        model_id = resolve_model(user, req.model)
        prompt = req.prompt if isinstance(req.prompt, str) else "".join(req.prompt)
        usage: dict = {}
        token_stream = stream_generate(
            prompt,
            temperature=AUTOCOMPLETE_TEMPERATURE if req.temperature is None else req.temperature,
            suffix=req.suffix,
            usage=usage,
            model=config.MODELS[model_id]["ollama_model"],
            options=ollama_options(req.max_tokens, req.top_p, req.stop),
        )
        completion_id = f"cmpl-{secrets.token_hex(12)}"
        created = int(time.time())

        if req.stream:
            def make_chunk(token: str) -> dict:
                return {
                    "id": completion_id,
                    "object": "text_completion",
                    "created": created,
                    "model": model_id,
                    "choices": [{"index": 0, "text": token, "finish_reason": None}],
                }

            def make_final() -> dict:
                return {
                    "id": completion_id,
                    "object": "text_completion",
                    "created": created,
                    "model": model_id,
                    "choices": [{"index": 0, "text": "", "finish_reason": finish_reason(usage, req.max_tokens)}],
                    "usage": usage_block(usage),
                }

            return run_stream(user, model_id, token_stream, usage, make_chunk, make_final)

        text = collect(user, token_stream, usage)
        return {
            "id": completion_id,
            "object": "text_completion",
            "created": created,
            "model": model_id,
            "choices": [{"index": 0, "text": text, "finish_reason": finish_reason(usage, req.max_tokens)}],
            "usage": usage_block(usage),
        }
    except ApiError as exc:
        return error_response(exc)
