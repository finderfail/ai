from __future__ import annotations

import sqlite3
from pathlib import Path

from rag import config

DB_PATH = Path(config.ROOT_DIR) / "data" / "platform.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    salt TEXT NOT NULL,
    plan TEXT NOT NULL DEFAULT 'free',
    language TEXT NOT NULL DEFAULT 'ru',
    governance INTEGER NOT NULL DEFAULT 0,
    model TEXT NOT NULL DEFAULT 'kriloud',
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS sessions (
    token TEXT PRIMARY KEY,
    user_id INTEGER NOT NULL,
    created_at TEXT NOT NULL,
    expires_at TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS usage_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    prompt_tokens INTEGER NOT NULL DEFAULT 0,
    completion_tokens INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL,
    day TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS access_keys (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    key_hash TEXT NOT NULL UNIQUE,
    prefix TEXT NOT NULL,
    created_at TEXT NOT NULL,
    last_used_at TEXT,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_usage_user_day ON usage_events (user_id, day);
CREATE INDEX IF NOT EXISTS idx_sessions_user ON sessions (user_id);
CREATE INDEX IF NOT EXISTS idx_access_keys_user ON access_keys (user_id);
"""

LEGACY_USAGE_REBUILD = """
DROP INDEX IF EXISTS idx_usage_user_day;
DROP INDEX IF EXISTS idx_usage_key_day;
ALTER TABLE usage_events RENAME TO usage_events_legacy;
CREATE TABLE usage_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    prompt_tokens INTEGER NOT NULL DEFAULT 0,
    completion_tokens INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL,
    day TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);
INSERT INTO usage_events (id, user_id, prompt_tokens, completion_tokens, created_at, day)
    SELECT id, user_id, prompt_tokens, completion_tokens, created_at, day
    FROM usage_events_legacy;
DROP TABLE usage_events_legacy;
"""


def connect() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA journal_mode = WAL")
    return conn


def _columns(conn: sqlite3.Connection, table: str) -> set[str]:
    return {row["name"] for row in conn.execute(f"PRAGMA table_info({table})")}


def init_db() -> None:
    conn = connect()
    try:
        conn.executescript(SCHEMA)
        if "plan" not in _columns(conn, "users"):
            conn.execute("ALTER TABLE users ADD COLUMN plan TEXT NOT NULL DEFAULT 'pro'")
        if "language" not in _columns(conn, "users"):
            conn.execute("ALTER TABLE users ADD COLUMN language TEXT NOT NULL DEFAULT 'ru'")
        if "governance" not in _columns(conn, "users"):
            conn.execute("ALTER TABLE users ADD COLUMN governance INTEGER NOT NULL DEFAULT 0")
        if "model" not in _columns(conn, "users"):
            conn.execute("ALTER TABLE users ADD COLUMN model TEXT NOT NULL DEFAULT 'kriloud'")
        if "mode" in _columns(conn, "usage_events"):
            conn.executescript(LEGACY_USAGE_REBUILD)
            conn.executescript(SCHEMA)
        conn.commit()
    finally:
        conn.close()
