from __future__ import annotations

import json
import secrets

import requests
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from rag import config
from rag.pipeline import answer_stream

from . import accounts, i18n
from .model_queue import closing_stream, queued
from .openai_api import (
    ApiError,
    authenticate,
    client_prompt,
    merge_options,
    ollama_options,
    resolve_model,
    text_of,
)

router = APIRouter(prefix="/v1")

ERROR_TYPES = {
    400: "invalid_request_error",
    401: "authentication_error",
    403: "permission_error",
    404: "not_found_error",
    429: "rate_limit_error",
}


class MessagesRequest(BaseModel):
    model: str | None = None
    messages: list[dict]
    system: str | list[dict] | None = None
    max_tokens: int | None = None
    stream: bool = False
    temperature: float | None = None
    top_p: float | None = None
    stop_sequences: list[str] | None = None


def anthropic_error(exc: ApiError) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status,
        content={
            "type": "error",
            "error": {"type": ERROR_TYPES.get(exc.status, "api_error"), "message": exc.message},
        },
    )


def block_text(content) -> str:
    if isinstance(content, list):
        content = [part for part in content if not isinstance(part, dict) or part.get("type") == "text"]
    return text_of(content)


def split(req: MessagesRequest) -> tuple[str, list[dict], str]:
    system = block_text(req.system) if req.system else ""
    dialog: list[dict] = []
    for message in req.messages:
        role = message.get("role")
        content = block_text(message.get("content"))
        if role in ("user", "assistant") and content:
            if dialog and dialog[-1]["role"] == role:
                dialog[-1]["content"] += "\n\n" + content
            else:
                dialog.append({"role": role, "content": content})
    question = dialog.pop()["content"] if dialog and dialog[-1]["role"] == "user" else ""
    return system, dialog, question


def stop_reason(usage: dict, max_tokens: int | None) -> str:
    if max_tokens and usage.get("completion_tokens", 0) >= max_tokens:
        return "max_tokens"
    return "end_turn"


def event(name: str, payload: dict) -> str:
    return f"event: {name}\ndata: {json.dumps(payload, ensure_ascii=False)}\n\n"


def estimate_tokens(text: str) -> int:
    return max(1, len(text) // 3)


@router.post("/messages/count_tokens")
def count_tokens(req: MessagesRequest, request: Request):
    try:
        authenticate(request)
    except ApiError as exc:
        return anthropic_error(exc)
    system, dialog, question = split(req)
    text = "\n".join([system, question, *(m["content"] for m in dialog)])
    return {"input_tokens": estimate_tokens(text)}


@router.post("/messages")
def messages(req: MessagesRequest, request: Request):
    try:
        user = authenticate(request)
        model_id = resolve_model(user, req.model, aliases=True)
        system, history, question = split(req)
        if not question:
            raise ApiError(400, "messages must end with a user message", "invalid_request_error", "invalid_messages")
        profile = config.model_request(model_id, history)
        options = merge_options(profile.pop("options"), ollama_options(req.max_tokens, req.top_p, req.stop_sequences))
        style = profile.pop("client_system")
        if req.temperature is not None:
            profile["temperature"] = req.temperature
        usage: dict = {}
        _, token_stream = answer_stream(
            question,
            usage=usage,
            language=user.language,
            domains=user.rag_domains,
            client_system=client_prompt(system, style),
            options=options,
            **profile,
        )
    except ApiError as exc:
        return anthropic_error(exc)

    message_id = f"msg_{secrets.token_hex(12)}"
    requested_model = req.model or model_id

    if not req.stream:
        try:
            text = "".join(value for kind, value in queued(token_stream) if kind == "token")
        except requests.RequestException:
            return anthropic_error(ApiError(502, i18n.text("model_timeout", user.language), "api_error", "upstream_error"))
        finally:
            accounts.record_usage(user.id, usage.get("prompt_tokens", 0), usage.get("completion_tokens", 0))
        return {
            "id": message_id,
            "type": "message",
            "role": "assistant",
            "model": requested_model,
            "content": [{"type": "text", "text": text}],
            "stop_reason": stop_reason(usage, req.max_tokens),
            "stop_sequence": None,
            "usage": {
                "input_tokens": usage.get("prompt_tokens", 0),
                "output_tokens": usage.get("completion_tokens", 0),
            },
        }

    def events():
        yield event(
            "message_start",
            {
                "type": "message_start",
                "message": {
                    "id": message_id,
                    "type": "message",
                    "role": "assistant",
                    "model": requested_model,
                    "content": [],
                    "stop_reason": None,
                    "stop_sequence": None,
                    "usage": {"input_tokens": 0, "output_tokens": 0},
                },
            },
        )
        yield event("content_block_start", {"type": "content_block_start", "index": 0, "content_block": {"type": "text", "text": ""}})
        try:
            for kind, value in queued(token_stream):
                if kind == "token":
                    yield event(
                        "content_block_delta",
                        {"type": "content_block_delta", "index": 0, "delta": {"type": "text_delta", "text": value}},
                    )
                else:
                    yield event("ping", {"type": "ping"})
        except requests.RequestException:
            yield event(
                "error",
                {"type": "error", "error": {"type": "api_error", "message": i18n.text("model_timeout", user.language)}},
            )
            return
        finally:
            accounts.record_usage(user.id, usage.get("prompt_tokens", 0), usage.get("completion_tokens", 0))
        yield event("content_block_stop", {"type": "content_block_stop", "index": 0})
        yield event(
            "message_delta",
            {
                "type": "message_delta",
                "delta": {"stop_reason": stop_reason(usage, req.max_tokens), "stop_sequence": None},
                "usage": {
                    "input_tokens": usage.get("prompt_tokens", 0),
                    "output_tokens": usage.get("completion_tokens", 0),
                },
            },
        )
        yield event("message_stop", {"type": "message_stop"})

    return closing_stream(events())
