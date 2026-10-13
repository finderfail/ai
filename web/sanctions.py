from __future__ import annotations

import json
import threading
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from rag import config

SANCTIONS_PATH = Path(config.ROOT_DIR) / "data" / "sanctions.json"

REASONS = {
    "USER_SANCTIONED": "Аккаунт заблокирован: санкции на пользователя",
    "COMPANY_SANCTIONED": "Аккаунт заблокирован: санкции на организацию",
    "SANCTIONED_COUNTRY": "Доступ закрыт: пользователь из санкционной страны",
    "ABUSE_DETECTED": "Доступ приостановлен: зафиксировано злоупотребление",
    "PAYMENT_FRAUD": "Доступ приостановлен: подозрение на мошенничество с оплатой",
    "MANUAL_REVIEW": "Доступ приостановлен: аккаунт на ручной проверке",
}

DEFAULT_REASON = "Доступ к сервису ограничен"

_lock = threading.Lock()
_cache: dict | None = None
_mtime: float | None = None


@dataclass
class Block:
    reason: str
    message: str
    note: str
    scope: str

    def to_dict(self) -> dict:
        return {
            "blocked": True,
            "reason": self.reason,
            "message": self.message,
            "note": self.note,
            "scope": self.scope,
        }


def _empty() -> dict:
    return {
        "enabled": True,
        "blocked_emails": [],
        "blocked_domains": [],
        "blocked_countries": [],
    }


def load() -> dict:
    global _cache, _mtime

    with _lock:
        if not SANCTIONS_PATH.exists():
            _cache = _empty()
            _mtime = None
            return _cache

        current = SANCTIONS_PATH.stat().st_mtime
        if _cache is not None and _mtime == current:
            return _cache

        try:
            data = json.loads(SANCTIONS_PATH.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return _cache if _cache is not None else _empty()

        merged = _empty()
        merged.update({k: v for k, v in data.items() if not k.startswith("_")})
        _cache = merged
        _mtime = current
        return _cache


def message_for(reason: str) -> str:
    return REASONS.get(reason, DEFAULT_REASON)


def _make_block(entry: dict, scope: str) -> Block:
    reason = entry.get("reason", "MANUAL_REVIEW")
    return Block(
        reason=reason,
        message=message_for(reason),
        note=entry.get("note", ""),
        scope=scope,
    )


def check_email(email: str | None) -> Block | None:
    if not email:
        return None

    data = load()
    if not data.get("enabled", True):
        return None

    normalized = email.strip().lower()
    domain = normalized.split("@")[-1] if "@" in normalized else ""

    for entry in data.get("blocked_emails", []):
        if str(entry.get("email", "")).strip().lower() == normalized:
            return _make_block(entry, "email")

    for entry in data.get("blocked_domains", []):
        if domain and str(entry.get("domain", "")).strip().lower() == domain:
            return _make_block(entry, "domain")

    return None


def check_country(country_code: str | None) -> Block | None:
    if not country_code:
        return None

    data = load()
    if not data.get("enabled", True):
        return None

    code = country_code.strip().upper()
    for entry in data.get("blocked_countries", []):
        if str(entry.get("code", "")).strip().upper() == code:
            return _make_block(entry, "country")

    return None


def check(email: str | None = None, country: str | None = None) -> Block | None:
    return check_email(email) or check_country(country)


def _read_raw() -> dict:
    if not SANCTIONS_PATH.exists():
        return _empty()
    data = json.loads(SANCTIONS_PATH.read_text(encoding="utf-8"))
    for key, value in _empty().items():
        data.setdefault(key, value)
    return data


def _write_raw(data: dict) -> None:
    global _cache, _mtime
    SANCTIONS_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = SANCTIONS_PATH.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(SANCTIONS_PATH)
    with _lock:
        _cache = None
        _mtime = None


def _upsert(section: str, field: str, value: str, reason: str, note: str) -> dict:
    if reason not in REASONS:
        raise ValueError(f"Причина должна быть одной из: {', '.join(REASONS)}")
    value = value.strip().lower()
    data = _read_raw()
    entries = [e for e in data[section] if str(e.get(field, "")).strip().lower() != value]
    entry = {field: value, "reason": reason, "note": note, "since": date.today().isoformat()}
    entries.append(entry)
    data[section] = entries
    _write_raw(data)
    return entry


def _remove(section: str, field: str, value: str) -> bool:
    value = value.strip().lower()
    data = _read_raw()
    before = len(data[section])
    data[section] = [e for e in data[section] if str(e.get(field, "")).strip().lower() != value]
    if len(data[section]) == before:
        return False
    _write_raw(data)
    return True


def block_email(email: str, reason: str = "USER_SANCTIONED", note: str = "") -> dict:
    return _upsert("blocked_emails", "email", email, reason, note)


def unblock_email(email: str) -> bool:
    return _remove("blocked_emails", "email", email)


def block_domain(domain: str, reason: str = "COMPANY_SANCTIONED", note: str = "") -> dict:
    return _upsert("blocked_domains", "domain", domain, reason, note)


def unblock_domain(domain: str) -> bool:
    return _remove("blocked_domains", "domain", domain)


def listing() -> dict:
    data = _read_raw()
    return {
        "enabled": data.get("enabled", True),
        "emails": data["blocked_emails"],
        "domains": data["blocked_domains"],
    }
