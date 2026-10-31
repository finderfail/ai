from __future__ import annotations

import hashlib
import json
import sqlite3
import threading
import time
from collections.abc import Iterator
from dataclasses import dataclass

from . import config
from .lexical import tokenize

_local = threading.local()
origin = "live"
_stats = {"hits": 0, "misses": 0, "stored": 0}
_stats_lock = threading.Lock()

SCHEMA = """
CREATE TABLE IF NOT EXISTS answers (
    key TEXT PRIMARY KEY,
    question TEXT NOT NULL,
    model TEXT NOT NULL,
    language TEXT NOT NULL,
    hints TEXT NOT NULL,
    answer TEXT NOT NULL,
    prompt_tokens INTEGER NOT NULL,
    completion_tokens INTEGER NOT NULL,
    origin TEXT NOT NULL,
    created_at REAL NOT NULL,
    used_at REAL NOT NULL,
    hits INTEGER NOT NULL DEFAULT 0
);
CREATE INDEX IF NOT EXISTS answers_used ON answers (used_at);
"""


@dataclass
class CachedAnswer:
    answer: str
    prompt_tokens: int
    completion_tokens: int


def _db() -> sqlite3.Connection | None:
    conn = getattr(_local, "conn", None)
    if conn is not None:
        return conn
    try:
        config.INDEX_DIR.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(config.CACHE_DB_PATH, timeout=2.0)
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA synchronous=NORMAL")
        conn.executescript(SCHEMA)
    except sqlite3.Error:
        return None
    _local.conn = conn
    return conn


def _hash(*parts: str) -> str:
    return hashlib.blake2b("\x1f".join(parts).encode("utf-8"), digest_size=16).hexdigest()


FILLER_WORDS = (
    "что такое это эта этот расскажи расскажите рассказать про о об обо пожалуйста плиз пж "
    "мне меня нам нас можно подскажи подскажите подсказать скажи скажите сказать "
    "объясни объясните объяснить у тебя тебе вас вам ты вы есть такой такая такое такие "
    "ли же а и в во на с со по для вообще просто вот ну "
    "please tell me about what is are the a an of explain"
)
SYNONYMS = {
    "гит": "git",
    "гитхаб": "github",
    "баш": "bash",
    "линукс": "linux",
    "джаваскрипт": "javascript",
    "жс": "js",
    "нода": "node",
    "ноде": "node",
    "экспресс": "express",
    "цсс": "css",
    "хтмл": "html",
}
FILLERS = set(tokenize(FILLER_WORDS)) | {"а", "и", "в", "с", "о", "у"}
SYNONYM_TOKENS = {tokenize(k)[0]: v for k, v in SYNONYMS.items()}


def question_key(question: str) -> str:
    tokens = [SYNONYM_TOKENS.get(t, t) for t in tokenize(question)]
    return " ".join(t for t in tokens if t not in FILLERS)


def profile_signature(params: dict, language: str) -> str:
    payload = {
        "params": params,
        "language": config.LANGUAGES.get(language, {}).get("instruction", language),
        "prompts": [
            config.SYSTEM_PROMPT,
            config.RAG_PROMPT_SUFFIX,
            config.FACT_RULES,
            config.CONTEXT_HEADER,
            config.CONTEXT_FOOTER,
            config.FLASH_SYSTEM_PROMPT,
            config.FLASH_HINT_CHARS,
        ],
    }
    return _hash(json.dumps(payload, ensure_ascii=False, sort_keys=True, default=str))


def hints_signature(hits) -> str:
    return _hash(*(chunk.text for chunk, _ in hits)) if hits else "none"


def _entry_key(profile: str, question: str, hints: str) -> str:
    return _hash(profile, question_key(question), hints)


def lookup(profile: str, question: str, hints: str) -> CachedAnswer | None:
    if not config.ANSWER_CACHE or not question_key(question):
        return None
    conn = _db()
    if conn is None:
        return None
    key = _entry_key(profile, question, hints)
    try:
        row = conn.execute(
            "SELECT answer, prompt_tokens, completion_tokens, origin, created_at FROM answers WHERE key = ?",
            (key,),
        ).fetchone()
        fresh = row is not None and (
            row[3] == "precache" or time.time() - row[4] < config.ANSWER_CACHE_TTL_DAYS * 86400
        )
        if fresh:
            conn.execute("UPDATE answers SET hits = hits + 1, used_at = ? WHERE key = ?", (time.time(), key))
            conn.commit()
    except sqlite3.Error:
        return None
    with _stats_lock:
        _stats["hits" if fresh else "misses"] += 1
    return CachedAnswer(row[0], row[1], row[2]) if fresh else None


def store(
    profile: str,
    model: str,
    language: str,
    question: str,
    hints: str,
    answer: str,
    usage: dict,
) -> None:
    if not config.ANSWER_CACHE or not answer.strip() or not question_key(question):
        return
    conn = _db()
    if conn is None:
        return
    now = time.time()
    try:
        conn.execute(
            "INSERT OR REPLACE INTO answers (key, question, model, language, hints, answer, "
            "prompt_tokens, completion_tokens, origin, created_at, used_at, hits) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0)",
            (
                _entry_key(profile, question, hints),
                question,
                model,
                language,
                hints,
                answer,
                int(usage.get("prompt_tokens", 0) or 0),
                int(usage.get("completion_tokens", 0) or 0),
                origin,
                now,
                now,
            ),
        )
        conn.execute(
            "DELETE FROM answers WHERE origin = 'live' AND key IN ("
            "SELECT key FROM answers WHERE origin = 'live' ORDER BY used_at DESC LIMIT -1 OFFSET ?)",
            (config.ANSWER_CACHE_MAX_ROWS,),
        )
        conn.commit()
    except sqlite3.Error:
        return
    with _stats_lock:
        _stats["stored"] += 1


def replay(cached: CachedAnswer, usage: dict | None) -> Iterator[str]:
    if usage is not None:
        usage["prompt_tokens"] = cached.prompt_tokens
        usage["completion_tokens"] = cached.completion_tokens
        usage["cached"] = True
    return iter([cached.answer])


def recording(token_stream, on_complete) -> Iterator[str]:
    parts: list[str] = []
    completed = False
    try:
        for token in token_stream:
            parts.append(token)
            yield token
        completed = True
    finally:
        token_stream.close()
        if completed:
            on_complete("".join(parts))


def popular(limit: int) -> list[tuple[str, str, str]]:
    conn = _db()
    if conn is None:
        return []
    rows = conn.execute(
        "SELECT question, model, language FROM answers ORDER BY hits DESC, used_at DESC LIMIT ?",
        (limit,),
    ).fetchall()
    return [(q, m, lang) for q, m, lang in rows]


def stats() -> dict:
    conn = _db()
    total = 0
    if conn is not None:
        try:
            total = conn.execute("SELECT count(*) FROM answers").fetchone()[0]
        except sqlite3.Error:
            pass
    with _stats_lock:
        return {**_stats, "entries": total}
