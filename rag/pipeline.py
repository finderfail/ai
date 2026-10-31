from __future__ import annotations

import re
import threading
import time
from collections import OrderedDict
from collections.abc import Iterator

from . import answer_cache, calculator, config, currency
from .embeddings import embed_query, normalize_query
from .llm import stream_chat
from .store import Chunk, VectorStore, flatten

_store: VectorStore | None = None
_store_lock = threading.Lock()
_checked_at = 0.0
_retrieval_cache: OrderedDict[tuple, list[tuple[Chunk, float]]] = OrderedDict()
_cache_lock = threading.Lock()

STORE_CHECK_SECONDS = 2.0
CJK_RE = re.compile(r"[\u3040-\u30ff\u3400-\u9fff\uff66-\uff9f]")
CYRILLIC_RE = re.compile(r"[а-яА-ЯёЁ]")


def _get_store() -> VectorStore:
    global _store, _checked_at
    now = time.monotonic()
    if _store is not None and now - _checked_at < STORE_CHECK_SECONDS:
        return _store
    with _store_lock:
        _checked_at = now
        try:
            version = config.INDEX_DB_PATH.stat().st_mtime
        except OSError:
            version = None
        if _store is None or (version is not None and version != _store.version):
            _store = VectorStore.load()
            with _cache_lock:
                _retrieval_cache.clear()
    return _store


def is_cross_lingual(query: str) -> bool:
    return bool(CJK_RE.search(query)) and not CYRILLIC_RE.search(query)


def retrieval_cache_stats() -> dict:
    with _cache_lock:
        return {"size": len(_retrieval_cache)}


LATIN_WORD_RE = re.compile(r"[A-Za-z][A-Za-z0-9&+.-]*")
ACRONYM_RE = re.compile(r"\b[А-ЯЁ]{2,6}\b")


def query_phrases(query: str) -> set[str]:
    phrases: set[str] = set()
    raw_words = LATIN_WORD_RE.findall(query)
    words = [w.lower().strip(".-") for w in raw_words]
    phrases.update(w.lower() for w in raw_words if 2 <= len(w) <= 6 and w.isupper())
    phrases.update(w.lower() for w in ACRONYM_RE.findall(query))
    for size in (2, 3):
        for i in range(len(words) - size + 1):
            phrases.add(" ".join(words[i : i + size]))
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
    query = normalize_query(query)
    domains = scope_domains(query, domains)
    store = _get_store()
    key = (query, frozenset(domains), limit, margin, store.version)
    with _cache_lock:
        cached = _retrieval_cache.get(key)
        if cached is not None:
            _retrieval_cache.move_to_end(key)
            return list(cached)

    selected = _retrieve(store, query, domains, limit, margin)

    with _cache_lock:
        _retrieval_cache[key] = selected
        while len(_retrieval_cache) > config.RETRIEVAL_CACHE_SIZE:
            _retrieval_cache.popitem(last=False)
    return list(selected)


def _retrieve(
    store: VectorStore,
    query: str,
    domains: set[str],
    limit: int | None,
    margin: float | None,
) -> list[tuple[Chunk, float]]:
    query_vector = embed_query(query)
    all_scores = store.embeddings @ query_vector
    cross_lingual = is_cross_lingual(query)
    threshold = config.RELEVANCE_THRESHOLD
    if not cross_lingual:
        hits = store.search(query_vector, domains=domains, scores=all_scores)
    else:
        threshold = config.CROSS_LINGUAL_THRESHOLD
        content = domains - config.CROSS_LINGUAL_STYLE_DOMAINS
        hits = store.search(query_vector, domains=content, scores=all_scores)
        if not hits or hits[0][1] < threshold:
            threshold = config.CROSS_LINGUAL_STYLE_THRESHOLD
            hits = store.search(
                query_vector, domains=domains & config.CROSS_LINGUAL_STYLE_DOMAINS, scores=all_scores
            )
    if not hits:
        return []

    spread = float(all_scores.std())
    top_score = hits[0][1]
    z_score = (top_score - float(all_scores.mean())) / spread if spread > 0 else 0.0

    if top_score < threshold or z_score < config.RELEVANCE_Z_MIN:
        return []

    margin = config.RELEVANCE_MARGIN if margin is None else margin
    floor = max(threshold, top_score - margin)
    relevant = [(chunk, score) for chunk, score in hits if score >= floor]

    if store.lexical is not None:
        if not cross_lingual:
            coverage = max(store.lexical.query_coverage(query, chunk.id) for chunk, _ in relevant)
            if coverage < config.LEXICAL_COVERAGE_MIN:
                return []
        if config.ENTITY_FOCUS:
            relevant = focus_on_entities(store, query, relevant)

    selected: list[tuple[Chunk, float]] = []
    used = 0
    for chunk, score in relevant:
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

    domains = domains if domains is not None else config.RAG_DOMAINS
    hits = retrieve(question, domains=domains, language=language, limit=max_hints, margin=rag_margin)
    usage = {} if usage is None else usage
    params = {
        "ollama_model": ollama_model or config.OLLAMA_MODEL,
        "client_system": client_system,
        "temperature": temperature,
        "options": options,
        "max_hints": max_hints,
        "rag_margin": rag_margin,
        "compact": compact,
    }
    token_stream = _model_stream(question, history, usage, language, hits, **params)
    if history:
        return hits, token_stream

    profile = answer_cache.profile_signature(params, language)
    hints = answer_cache.hints_signature(hits)
    cached = answer_cache.lookup(profile, question, hints)
    if cached is not None:
        token_stream.close()
        return hits, answer_cache.replay(cached, usage)

    def remember(text: str) -> None:
        answer_cache.store(profile, params["ollama_model"], language, question, hints, text, usage)

    return hits, answer_cache.recording(token_stream, remember)


def _model_stream(
    question: str,
    history: list[dict] | None,
    usage: dict,
    language: str,
    hits: list[tuple[Chunk, float]],
    ollama_model: str,
    client_system: str | None,
    temperature: float | None,
    options: dict | None,
    max_hints: int | None,
    rag_margin: float | None,
    compact: bool,
) -> Iterator[str]:
    language_config = config.LANGUAGES.get(language, config.LANGUAGES[config.DEFAULT_LANGUAGE])
    if compact:
        system_prompt = config.FLASH_SYSTEM_PROMPT
        if hits:
            system_prompt = f"{system_prompt}\n\nСправка:\n{hits[0][0].text[: config.FLASH_HINT_CHARS]}"
        if client_system:
            system_prompt = f"{system_prompt}\n\n{client_system}"
        system_prompt = f"{system_prompt}\n\n{language_config['instruction']}"
        messages = [{"role": "system", "content": system_prompt}, *(history or []), {"role": "user", "content": question}]
        return stream_chat(
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

    return stream_chat(
        messages,
        temperature=config.TEMPERATURE if temperature is None else temperature,
        usage=usage,
        model=ollama_model,
        options=options,
    )
