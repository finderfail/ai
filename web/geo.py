from __future__ import annotations

import ipaddress
import json
import os
import threading
from pathlib import Path

from rag import config

GEO_PATH = Path(config.ROOT_DIR) / "data" / "geo.json"
COUNTRY_HEADER = os.getenv("GEO_COUNTRY_HEADER", "cf-ipcountry").lower()
UNKNOWN_CODES = {"", "XX", "T1"}

BLOCK_MESSAGE = "Sorry, Universal Kriloud AI is not available in your region."

BLOCK_PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Region not supported</title>
<style>
:root { color-scheme: light dark; }
body { margin: 0; min-height: 100vh; display: flex; align-items: center; justify-content: center;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
  background: #ffffff; color: #1c1c1f; padding: 24px; box-sizing: border-box; }
@media (prefers-color-scheme: dark) { body { background: #161618; color: #f1f1f4; } }
main { max-width: 420px; text-align: center; }
.orb { width: 64px; height: 64px; margin: 0 auto 20px; border-radius: 50%;
  background: conic-gradient(from 210deg, #8a5cff, #5b6bff, #3fa2ff, #b46bff, #ff6bd6, #8a5cff); }
h1 { font-size: 24px; margin: 0 0 10px; }
p { margin: 0; color: #74767e; line-height: 1.5; }
</style>
</head>
<body>
<main>
<div class="orb"></div>
<h1>Your region is not supported</h1>
<p>Sorry, Universal Kriloud AI is not available in your country or region.</p>
</main>
</body>
</html>
"""

_lock = threading.Lock()
_cache: dict | None = None
_mtime: float | None = None


def _default() -> dict:
    return {"enabled": False, "allowed": [], "unknown": "deny"}


def load() -> dict:
    global _cache, _mtime
    with _lock:
        if not GEO_PATH.exists():
            _cache, _mtime = _default(), None
            return _cache
        current = GEO_PATH.stat().st_mtime
        if _cache is not None and _mtime == current:
            return _cache
        try:
            data = json.loads(GEO_PATH.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return _cache if _cache is not None else _default()
        merged = _default()
        merged.update(data)
        merged["allowed"] = sorted({str(c).strip().upper() for c in merged["allowed"] if str(c).strip()})
        _cache, _mtime = merged, current
        return _cache


def save(data: dict) -> None:
    global _cache, _mtime
    GEO_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = GEO_PATH.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(GEO_PATH)
    with _lock:
        _cache, _mtime = None, None


def _is_local(host: str | None) -> bool:
    try:
        address = ipaddress.ip_address(host or "")
    except ValueError:
        return False
    return address.is_loopback or address.is_private


def country_of(headers, client_host: str | None) -> str | None:
    code = (headers.get(COUNTRY_HEADER) or "").strip().upper()
    if code and code not in UNKNOWN_CODES:
        return code
    return None


def is_allowed(headers, client_host: str | None) -> bool:
    data = load()
    if not data["enabled"]:
        return True
    country = country_of(headers, client_host)
    if country is not None:
        return country in data["allowed"]
    forwarded = headers.get("x-forwarded-for") or headers.get(COUNTRY_HEADER)
    if not forwarded and _is_local(client_host):
        return True
    return data["unknown"] == "allow"
