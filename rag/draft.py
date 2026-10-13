from __future__ import annotations

from . import config
from .llm import stream_chat
from .pipeline import build_context_block, retrieve


def _load_persona() -> str:
    if not config.PERSONA_DIR.exists():
        return ""
    files = sorted(config.PERSONA_DIR.glob("*.md"))
    if not files:
        return ""
    parts = [f.read_text(encoding="utf-8").strip() for f in files]
    return "\n\n---\n\n".join(parts)


def generate_draft(message: str) -> tuple[str, list[str]]:
    persona = _load_persona()
    hits = retrieve(message, domains={"boundaries"})

    system_prompt = config.DRAFT_SYSTEM_PROMPT
    if persona:
        system_prompt = f"{system_prompt}\n\nСТИЛЬ АККАУНТА:\n\n{persona}"
    if hits:
        context = build_context_block(hits)
        system_prompt = (
            f"{system_prompt}\n\n{config.CONTEXT_HEADER}\n\n{context}\n\n{config.CONTEXT_FOOTER}"
        )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Входящее сообщение: {message}"},
    ]

    draft = "".join(stream_chat(messages, temperature=config.DRAFT_TEMPERATURE))
    sources = sorted({f"{c.domain}/{c.source}" for c, _ in hits})
    return draft, sources
