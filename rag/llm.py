from __future__ import annotations

import json
from collections.abc import Iterator

import requests

from . import config


def check_ollama_available() -> tuple[bool, str]:
    try:
        resp = requests.get(f"{config.OLLAMA_HOST}/api/tags", timeout=3)
        resp.raise_for_status()
    except requests.RequestException as exc:
        return False, f"Ollama недоступна на {config.OLLAMA_HOST}: {exc}"

    models = [m["name"] for m in resp.json().get("models", [])]
    if not any(m.startswith(config.OLLAMA_MODEL) for m in models):
        return False, (
            f"Модель {config.OLLAMA_MODEL!r} не найдена в Ollama. "
            f"Выполните: ollama pull {config.OLLAMA_MODEL}"
        )
    return True, "ok"


def _options(temperature: float, overrides: dict | None) -> dict:
    options = {
        "temperature": temperature,
        "repeat_penalty": config.REPEAT_PENALTY,
        "top_p": config.TOP_P,
        "num_ctx": config.NUM_CTX,
    }
    if overrides:
        options.update({k: v for k, v in overrides.items() if v is not None})
    return options


def _stream(endpoint: str, payload: dict, usage: dict | None, extract) -> Iterator[str]:
    with requests.post(
        f"{config.OLLAMA_HOST}{endpoint}",
        json=payload,
        stream=True,
        timeout=config.OLLAMA_TIMEOUT,
    ) as resp:
        resp.raise_for_status()
        for line in resp.iter_lines():
            if not line:
                continue
            data = json.loads(line)
            if data.get("done"):
                if usage is not None:
                    usage["prompt_tokens"] = data.get("prompt_eval_count", 0)
                    usage["completion_tokens"] = data.get("eval_count", 0)
                break
            token = extract(data)
            if token:
                yield token


def stream_chat(
    messages: list[dict],
    temperature: float,
    usage: dict | None = None,
    model: str | None = None,
    options: dict | None = None,
) -> Iterator[str]:
    payload = {
        "model": model or config.OLLAMA_MODEL,
        "messages": messages,
        "stream": True,
        "think": False,
        "keep_alive": config.OLLAMA_KEEP_ALIVE,
        "options": _options(temperature, options),
    }
    return _stream("/api/chat", payload, usage, lambda d: d.get("message", {}).get("content", ""))


def stream_generate(
    prompt: str,
    temperature: float,
    suffix: str | None = None,
    usage: dict | None = None,
    model: str | None = None,
    options: dict | None = None,
) -> Iterator[str]:
    payload = {
        "model": model or config.OLLAMA_MODEL,
        "prompt": prompt,
        "stream": True,
        "keep_alive": config.OLLAMA_KEEP_ALIVE,
        "options": _options(temperature, options),
    }
    if suffix:
        payload["suffix"] = suffix
    return _stream("/api/generate", payload, usage, lambda d: d.get("response", ""))
