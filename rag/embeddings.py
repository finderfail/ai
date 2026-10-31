from __future__ import annotations

import hashlib
import sqlite3
import sys
import threading
import time
from collections import OrderedDict

import numpy as np

from . import config
from .encoder import BertEncoder, resolve_model_dir

_model: BertEncoder | None = None
_model_lock = threading.Lock()
_memory: OrderedDict[str, np.ndarray] = OrderedDict()
_memory_lock = threading.Lock()
_local = threading.local()
_stats = {"memory_hits": 0, "disk_hits": 0, "computed": 0}


def _get_model() -> BertEncoder:
    global _model
    if _model is None:
        with _model_lock:
            if _model is None:
                model_dir = resolve_model_dir(
                    config.EMBEDDING_MODEL_NAME, config.EMBEDDING_MODEL_DIR or None, config.EMBEDDING_LOCAL_DIR
                )
                _model = BertEncoder(model_dir)
    return _model


def _cache_db() -> sqlite3.Connection | None:
    conn = getattr(_local, "conn", None)
    if conn is not None:
        return conn
    try:
        config.INDEX_DIR.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(config.CACHE_DB_PATH, timeout=1.0)
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA synchronous=NORMAL")
        conn.execute(
            "CREATE TABLE IF NOT EXISTS query_vectors ("
            "key TEXT PRIMARY KEY, vector BLOB NOT NULL, used_at REAL NOT NULL)"
        )
    except sqlite3.Error:
        return None
    _local.conn = conn
    return conn


def _key(text: str) -> str:
    raw = f"{config.EMBEDDING_MODEL_NAME}\n{text}".encode("utf-8")
    return hashlib.blake2b(raw, digest_size=16).hexdigest()


def _remember(key: str, vector: np.ndarray) -> None:
    with _memory_lock:
        _memory[key] = vector
        _memory.move_to_end(key)
        while len(_memory) > config.QUERY_CACHE_SIZE:
            _memory.popitem(last=False)


def _disk_get(key: str) -> np.ndarray | None:
    conn = _cache_db()
    if conn is None:
        return None
    try:
        row = conn.execute("SELECT vector FROM query_vectors WHERE key = ?", (key,)).fetchone()
        if row is None:
            return None
        conn.execute("UPDATE query_vectors SET used_at = ? WHERE key = ?", (time.time(), key))
        conn.commit()
    except sqlite3.Error:
        return None
    return np.frombuffer(row[0], dtype=np.float32).copy()


def _disk_put(key: str, vector: np.ndarray) -> None:
    conn = _cache_db()
    if conn is None:
        return
    try:
        conn.execute(
            "INSERT OR REPLACE INTO query_vectors (key, vector, used_at) VALUES (?, ?, ?)",
            (key, vector.astype(np.float32).tobytes(), time.time()),
        )
        if _stats["computed"] % 500 == 0:
            conn.execute(
                "DELETE FROM query_vectors WHERE key IN ("
                "SELECT key FROM query_vectors ORDER BY used_at DESC LIMIT -1 OFFSET ?)",
                (config.QUERY_CACHE_DISK_ROWS,),
            )
        conn.commit()
    except sqlite3.Error:
        pass


def normalize_query(text: str) -> str:
    return " ".join(text.split())


def embed_passages(texts: list[str], show_progress: bool = False) -> np.ndarray:
    model = _get_model()
    done = [0]

    def progress(count: int) -> None:
        done[0] += count
        sys.stdout.write(f"\r  эмбеддинги: {done[0]}/{len(texts)}")
        sys.stdout.flush()

    vectors = model.encode(
        [f"passage: {t}" for t in texts],
        batch_size=config.EMBEDDING_BATCH_SIZE,
        on_batch=progress if show_progress else None,
    )
    if show_progress:
        sys.stdout.write("\n")
    return vectors


def embed_query(text: str) -> np.ndarray:
    text = normalize_query(text)
    key = _key(text)
    with _memory_lock:
        cached = _memory.get(key)
        if cached is not None:
            _memory.move_to_end(key)
            _stats["memory_hits"] += 1
            return cached
    vector = _disk_get(key)
    if vector is not None:
        _stats["disk_hits"] += 1
    else:
        vector = _get_model().encode([f"query: {text}"])[0]
        _stats["computed"] += 1
        _disk_put(key, vector)
    vector.setflags(write=False)
    _remember(key, vector)
    return vector


def cache_stats() -> dict:
    with _memory_lock:
        return {**_stats, "memory_size": len(_memory)}
