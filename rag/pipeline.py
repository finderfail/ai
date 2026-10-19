from __future__ import annotations

import re
from collections.abc import Iterator

from . import calculator, config, currency
from .embeddings import embed_query
from .llm import stream_chat
from .store import Chunk, VectorStore, flatten

_store: VectorStore | None = None


def _get_store() -> VectorStore:
    global _store
    if _store is None:
        _store = VectorStore.load()
    return _store


def localize(
    store: VectorStore, hits: list[tuple[Chunk, float]], language: str | None
) -> list[tuple[Chunk, float]]:
    seen: set[tuple[str, str]] = set()
    result: list[tuple[Chunk, float]] = []
    for chunk, score in hits:
        if chunk.base_key in seen:
            continue
        seen.add(chunk.base_key)
        result.append((store.variant(chunk, language) if language else chunk, score))
    return result


LATIN_WORD_RE = re.compile(r"[A-Za-z][A-Za-z0-9&+.-]*")
ACRONYM_RE = re.compile(r"\b[А-ЯЁ]{2,6}\b")
CJK_RUN_RE = re.compile(r"[\u3040-\u30ff\u3400-\u9fff\uff66-\uff9f]{3,}")


def query_phrases(query: str) -> set[str]:
    phrases: set[str] = set()
    raw_words = LATIN_WORD_RE.findall(query)
    words = [w.lower().strip(".-") for w in raw_words]
    phrases.update(w.lower() for w in raw_words if 2 <= len(w) <= 6 and w.isupper())
    phrases.update(w.lower() for w in ACRONYM_RE.findall(query))
    for size in (2, 3):
        for i in range(len(words) - size + 1):
            phrases.add(" ".join(words[i : i + size]))
    for run in CJK_RUN_RE.findall(query):
        for i in range(len(run) - 2):
            phrases.add(run[i : i + 3])
    return {p for p in phrases if len(p) >= 3 or (len(p) >= 2 and p.isalpha() and not p.isascii())}


def focus_on_entities(
    store: VectorStore, query: str, hits: list[tuple[Chunk, float]]
) -> list[tuple[Chunk, float]]:
    if len(hits) < 2:
        return hits
    phrases = {flatten(p) for p in query_phrases(query)} - {""}
    markers = [
        phrase
        for phrase in phrases
        if 1 <= sum(1 for text in store.lowered_texts if phrase in text) <= config.PHRASE_MAX_DF
    ]
    if markers:
        focused = [
            (chunk, score)
            for chunk, score in hits
            if any(m in store.lowered_texts[chunk.id] for m in markers)
        ]
        return focused or hits

    return hits


def scope_domains(query: str, domains: set[str]) -> set[str]:
    requested = {
        domain
        for domain, pattern in config.OPT_IN_DOMAINS.items()
        if domain in domains and re.search(pattern, query, re.IGNORECASE)
    }
    if requested:
        return requested
    return {domain for domain in domains if domain not in config.OPT_IN_DOMAINS}


def retrieve(
    query: str,
    domains: set[str],
    language: str | None = None,
    limit: int | None = None,
    margin: float | None = None,
) -> list[tuple[Chunk, float]]:
    domains = scope_domains(query, domains)
    store = _get_store()
    query_vector = embed_query(query)
    hits = store.search(query_vector, domains=domains)
    if not hits:
        return []

    all_scores = store.embeddings @ query_vector
    spread = float(all_scores.std())
    top_score = hits[0][1]
    z_score = (top_score - float(all_scores.mean())) / spread if spread > 0 else 0.0

    if top_score < config.RELEVANCE_THRESHOLD or z_score < config.RELEVANCE_Z_MIN:
        return []

    margin = config.RELEVANCE_MARGIN if margin is None else margin
    floor = max(config.RELEVANCE_THRESHOLD, top_score - margin)
    relevant = [(chunk, score) for chunk, score in hits if score >= floor]

    if store.lexical is not None:
        coverage = max(store.lexical.query_coverage(query, chunk.id) for chunk, _ in relevant)
        if coverage < config.LEXICAL_COVERAGE_MIN:
            return []
        if config.ENTITY_FOCUS:
            relevant = focus_on_entities(store, query, relevant)

    selected: list[tuple[Chunk, float]] = []
    used = 0
    for chunk, score in localize(store, relevant, language):
        if limit is not None and len(selected) >= limit:
            break
        if used + len(chunk.text) > config.CONTEXT_CHAR_BUDGET:
            break
        selected.append((chunk, score))
        used += len(chunk.text)
    return selected


def build_context_block(hits: list[tuple[Chunk, float]]) -> str:
    parts = [chunk.text for chunk, _ in reversed(hits)]
    return "\n\n---\n\n".join(parts)


def answer_stream(
    question: str,
    history: list[dict] | None = None,
    usage: dict | None = None,
    language: str = config.DEFAULT_LANGUAGE,
    domains: set[str] | None = None,
    ollama_model: str | None = None,
    client_system: str | None = None,
    temperature: float | None = None,
    options: dict | None = None,
    max_hints: int | None = None,
    rag_margin: float | None = None,
    compact: bool = False,
) -> tuple[list[tuple[Chunk, float]], Iterator[str]]:
    calculated = calculator.answer(question, language)
    if calculated:
        return [], iter([calculated])

    converted = currency.answer(question, language)
    if converted:
        return [], iter([converted])

    hits = retrieve(
        question,
        domains=domains if domains is not None else config.RAG_DOMAINS,
        language=language,
        limit=max_hints,
        margin=rag_margin,
    )

    language_config = config.LANGUAGES.get(language, config.LANGUAGES[config.DEFAULT_LANGUAGE])
    if compact:
        system_prompt = config.FLASH_SYSTEM_PROMPT
        if hits:
            system_prompt = f"{system_prompt}\n\nСправка:\n{hits[0][0].text[: config.FLASH_HINT_CHARS]}"
        if client_system:
            system_prompt = f"{system_prompt}\n\n{client_system}"
        system_prompt = f"{system_prompt}\n\n{language_config['instruction']}"
        messages = [{"role": "system", "content": system_prompt}, *(history or []), {"role": "user", "content": question}]
        return hits, stream_chat(
            messages,
            temperature=config.TEMPERATURE if temperature is None else temperature,
            usage=usage,
            model=ollama_model,
            options=options,
        )

    system_prompt = f"{config.SYSTEM_PROMPT} {config.RAG_PROMPT_SUFFIX} {config.FACT_RULES}"
    if hits:
        context = build_context_block(hits)
        system_prompt = (
            f"{system_prompt}\n\n{config.CONTEXT_HEADER}\n\n{context}\n\n{config.CONTEXT_FOOTER}"
        )
    if client_system:
        system_prompt = f"{system_prompt}\n\n{client_system}"
    system_prompt = f"{system_prompt}\n\n{language_config['instruction']}"

    messages = [{"role": "system", "content": system_prompt}]
    if history:
        messages.extend(history)
    messages.append({"role": "user", "content": question})

    return hits, stream_chat(
        messages,
        temperature=config.TEMPERATURE if temperature is None else temperature,
        usage=usage,
        model=ollama_model,
        options=options,
    )
