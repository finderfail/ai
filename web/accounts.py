from __future__ import annotations

import hashlib
import hmac
import os
import re
import secrets
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

from rag import config

from . import db, i18n

SESSION_TTL_DAYS = int(os.getenv("SESSION_TTL_DAYS", "30"))

PLAN_FREE = "free"
PLAN_PRO = "pro"
PLAN_UNLIMITED = "unlimited"

PLANS = {
    PLAN_FREE: {
        "label": "Free",
        "daily_token_limit": int(os.getenv("FREE_DAILY_TOKEN_LIMIT", "10000")),
    },
    PLAN_PRO: {
        "label": "Pro",
        "daily_token_limit": int(os.getenv("PRO_DAILY_TOKEN_LIMIT", "1000000")),
    },
    PLAN_UNLIMITED: {
        "label": "Unlimited",
        "daily_token_limit": None,
    },
}

DEFAULT_PLAN = PLAN_FREE

ACCESS_KEY_PREFIX = "ukai-"
MAX_ACCESS_KEYS = int(os.getenv("MAX_ACCESS_KEYS", "10"))

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class AccountError(Exception):
    def __init__(self, key: str, **params):
        self.key = key
        self.params = params
        super().__init__(i18n.text(key, **params))

    def message(self, language: str | None) -> str:
        return i18n.text(self.key, language, **self.params)


@dataclass
class User:
    id: int
    email: str
    plan: str
    created_at: str
    language: str = config.DEFAULT_LANGUAGE
    governance: bool = False
    model: str = config.DEFAULT_MODEL

    @property
    def plan_label(self) -> str:
        return PLANS.get(self.plan, PLANS[DEFAULT_PLAN])["label"]

    @property
    def active_model(self) -> str:
        if self.model in self.available_models:
            return self.model
        return config.DEFAULT_MODEL

    @property
    def available_models(self) -> list[str]:
        return [
            model_id
            for model_id, model in config.MODELS.items()
            if self.governance or not model["governance_only"]
        ]

    @property
    def rag_domains(self) -> set[str]:
        if self.governance:
            return config.RAG_DOMAINS | config.GOVERNANCE_DOMAINS
        return set(config.RAG_DOMAINS)

    @property
    def daily_limit(self) -> int | None:
        return PLANS.get(self.plan, PLANS[DEFAULT_PLAN])["daily_token_limit"]


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _iso(value: datetime) -> str:
    return value.isoformat()


def _today() -> str:
    return _now().date().isoformat()


def _hash_password(password: str, salt: str) -> str:
    derived = hashlib.scrypt(
        password.encode("utf-8"),
        salt=bytes.fromhex(salt),
        n=2**14,
        r=8,
        p=1,
        dklen=32,
    )
    return derived.hex()


def _row_to_user(row: sqlite3.Row) -> User:
    return User(
        id=row["id"],
        email=row["email"],
        plan=row["plan"] if row["plan"] in PLANS else DEFAULT_PLAN,
        created_at=row["created_at"],
        language=row["language"] if row["language"] in config.LANGUAGES else config.DEFAULT_LANGUAGE,
        governance=bool(row["governance"]),
        model=row["model"] if row["model"] in config.MODELS else config.DEFAULT_MODEL,
    )


def _normalize_email(email: str | None) -> str:
    return (email or "").strip().lower()


def validate_credentials(email: str, password: str) -> None:
    if not EMAIL_RE.match(email or ""):
        raise AccountError("invalid_email")
    if len(password or "") < 8:
        raise AccountError("short_password")


def register(
    email: str,
    password: str,
    plan: str = DEFAULT_PLAN,
    language: str = config.DEFAULT_LANGUAGE,
) -> User:
    email = _normalize_email(email)
    validate_credentials(email, password)
    if plan not in PLANS:
        raise AccountError("unknown_plan", plans=", ".join(PLANS))
    if language not in config.LANGUAGES:
        language = config.DEFAULT_LANGUAGE

    salt = secrets.token_hex(16)
    password_hash = _hash_password(password, salt)
    created_at = _iso(_now())

    conn = db.connect()
    try:
        cur = conn.execute(
            """
            INSERT INTO users (email, password_hash, salt, plan, language, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (email, password_hash, salt, plan, language, created_at),
        )
        conn.commit()
        user_id = cur.lastrowid
    except sqlite3.IntegrityError:
        raise AccountError("email_taken")
    finally:
        conn.close()

    return User(id=user_id, email=email, plan=plan, created_at=created_at, language=language)


def authenticate(email: str, password: str) -> User:
    email = _normalize_email(email)
    conn = db.connect()
    try:
        row = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    finally:
        conn.close()

    if row is None:
        raise AccountError("bad_credentials")

    candidate = _hash_password(password or "", row["salt"])
    if not hmac.compare_digest(candidate, row["password_hash"]):
        raise AccountError("bad_credentials")

    return _row_to_user(row)


def get_user_by_email(email: str) -> User | None:
    conn = db.connect()
    try:
        row = conn.execute(
            "SELECT * FROM users WHERE email = ?", (_normalize_email(email),)
        ).fetchone()
    finally:
        conn.close()
    return _row_to_user(row) if row else None


def list_users() -> list[User]:
    conn = db.connect()
    try:
        rows = conn.execute("SELECT * FROM users ORDER BY id").fetchall()
    finally:
        conn.close()
    return [_row_to_user(row) for row in rows]


def set_plan(email: str, plan: str) -> User:
    if plan not in PLANS:
        raise AccountError("unknown_plan", plans=", ".join(PLANS))
    conn = db.connect()
    try:
        conn.execute(
            "UPDATE users SET plan = ? WHERE email = ?", (plan, _normalize_email(email))
        )
        conn.commit()
    finally:
        conn.close()
    user = get_user_by_email(email)
    if user is None:
        raise AccountError("user_not_found")
    return user


def set_language(user_id: int, language: str) -> None:
    if language not in config.LANGUAGES:
        raise AccountError("unknown_language", languages=", ".join(config.LANGUAGES))
    conn = db.connect()
    try:
        conn.execute("UPDATE users SET language = ? WHERE id = ?", (language, user_id))
        conn.commit()
    finally:
        conn.close()


def set_governance(email: str, enabled: bool) -> User:
    conn = db.connect()
    try:
        if enabled:
            conn.execute(
                "UPDATE users SET governance = 1 WHERE email = ?", (_normalize_email(email),)
            )
        else:
            conn.execute(
                "UPDATE users SET governance = 0, model = ? WHERE email = ?",
                (config.DEFAULT_MODEL, _normalize_email(email)),
            )
        conn.commit()
    finally:
        conn.close()
    user = get_user_by_email(email)
    if user is None:
        raise AccountError("user_not_found")
    return user


def set_model(user: User, model: str) -> None:
    if model not in user.available_models:
        raise AccountError("unknown_model")
    conn = db.connect()
    try:
        conn.execute("UPDATE users SET model = ? WHERE id = ?", (model, user.id))
        conn.commit()
    finally:
        conn.close()


def languages_overview() -> list[dict]:
    return [{"id": code, "label": lang["label"]} for code, lang in config.LANGUAGES.items()]


def _hash_access_key(raw_key: str) -> str:
    return hashlib.sha256(raw_key.encode("utf-8")).hexdigest()


def list_access_keys(user_id: int) -> list[dict]:
    conn = db.connect()
    try:
        rows = conn.execute(
            """
            SELECT id, name, prefix, created_at, last_used_at
            FROM access_keys WHERE user_id = ? ORDER BY id DESC
            """,
            (user_id,),
        ).fetchall()
    finally:
        conn.close()
    return [dict(row) for row in rows]


def create_access_key(user_id: int, name: str) -> dict:
    name = (name or "").strip()[:64] or "default"
    conn = db.connect()
    try:
        count = conn.execute(
            "SELECT COUNT(*) FROM access_keys WHERE user_id = ?", (user_id,)
        ).fetchone()[0]
        if count >= MAX_ACCESS_KEYS:
            raise AccountError("key_limit", limit=MAX_ACCESS_KEYS)
        raw_key = f"{ACCESS_KEY_PREFIX}{secrets.token_urlsafe(32)}"
        prefix = f"{raw_key[: len(ACCESS_KEY_PREFIX) + 4]}…{raw_key[-4:]}"
        created_at = _iso(_now())
        cur = conn.execute(
            """
            INSERT INTO access_keys (user_id, name, key_hash, prefix, created_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (user_id, name, _hash_access_key(raw_key), prefix, created_at),
        )
        conn.commit()
        key_id = cur.lastrowid
    finally:
        conn.close()
    return {
        "id": key_id,
        "name": name,
        "prefix": prefix,
        "created_at": created_at,
        "last_used_at": None,
        "key": raw_key,
    }


def delete_access_key(user_id: int, key_id: int) -> None:
    conn = db.connect()
    try:
        cur = conn.execute(
            "DELETE FROM access_keys WHERE id = ? AND user_id = ?", (key_id, user_id)
        )
        conn.commit()
    finally:
        conn.close()
    if cur.rowcount == 0:
        raise AccountError("key_not_found")


def user_by_access_key(raw_key: str | None) -> User | None:
    raw_key = (raw_key or "").strip()
    if not raw_key.startswith(ACCESS_KEY_PREFIX):
        return None
    key_hash = _hash_access_key(raw_key)
    conn = db.connect()
    try:
        row = conn.execute(
            """
            SELECT u.*, k.id AS key_id FROM access_keys k
            JOIN users u ON u.id = k.user_id
            WHERE k.key_hash = ?
            """,
            (key_hash,),
        ).fetchone()
        if row is None:
            return None
        conn.execute(
            "UPDATE access_keys SET last_used_at = ? WHERE id = ?",
            (_iso(_now()), row["key_id"]),
        )
        conn.commit()
    finally:
        conn.close()
    return _row_to_user(row)


def create_session(user_id: int) -> str:
    token = secrets.token_urlsafe(32)
    now = _now()
    conn = db.connect()
    try:
        conn.execute(
            "INSERT INTO sessions (token, user_id, created_at, expires_at) VALUES (?, ?, ?, ?)",
            (token, user_id, _iso(now), _iso(now + timedelta(days=SESSION_TTL_DAYS))),
        )
        conn.commit()
    finally:
        conn.close()
    return token


def user_by_session(token: str | None) -> User | None:
    if not token:
        return None
    conn = db.connect()
    try:
        row = conn.execute(
            """
            SELECT u.* FROM sessions s
            JOIN users u ON u.id = s.user_id
            WHERE s.token = ? AND s.expires_at > ?
            """,
            (token, _iso(_now())),
        ).fetchone()
    finally:
        conn.close()
    return _row_to_user(row) if row else None


def delete_session(token: str | None) -> None:
    if not token:
        return
    conn = db.connect()
    try:
        conn.execute("DELETE FROM sessions WHERE token = ?", (token,))
        conn.commit()
    finally:
        conn.close()


def record_usage(user_id: int, prompt_tokens: int, completion_tokens: int) -> None:
    now = _now()
    conn = db.connect()
    try:
        conn.execute(
            """
            INSERT INTO usage_events (user_id, prompt_tokens, completion_tokens, created_at, day)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                user_id,
                int(prompt_tokens or 0),
                int(completion_tokens or 0),
                _iso(now),
                now.date().isoformat(),
            ),
        )
        conn.commit()
    finally:
        conn.close()


def tokens_used_today(user_id: int) -> int:
    conn = db.connect()
    try:
        row = conn.execute(
            """
            SELECT COALESCE(SUM(prompt_tokens + completion_tokens), 0) AS total
            FROM usage_events WHERE user_id = ? AND day = ?
            """,
            (user_id, _today()),
        ).fetchone()
    finally:
        conn.close()
    return int(row["total"])


def usage_by_day(user_id: int, days: int = 14) -> list[dict]:
    since = (_now() - timedelta(days=days - 1)).date().isoformat()
    conn = db.connect()
    try:
        rows = conn.execute(
            """
            SELECT day,
                   COUNT(*) AS requests,
                   COALESCE(SUM(prompt_tokens), 0) AS prompt_tokens,
                   COALESCE(SUM(completion_tokens), 0) AS completion_tokens
            FROM usage_events
            WHERE user_id = ? AND day >= ?
            GROUP BY day ORDER BY day DESC
            """,
            (user_id, since),
        ).fetchall()
    finally:
        conn.close()
    return [dict(row) for row in rows]


def quota_status(user: User) -> dict:
    used = tokens_used_today(user.id)
    limit = user.daily_limit
    return {
        "plan": user.plan,
        "plan_label": user.plan_label,
        "used_today": used,
        "limit": limit,
        "remaining": None if limit is None else max(0, limit - used),
        "exceeded": limit is not None and used >= limit,
    }


def plans_overview() -> list[dict]:
    return [
        {"id": plan_id, "label": plan["label"], "daily_token_limit": plan["daily_token_limit"]}
        for plan_id, plan in PLANS.items()
    ]
