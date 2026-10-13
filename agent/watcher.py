"""
Read-only watcher: следит за новым входящим сообщением в чате и просит
локальный backend (/api/draft) сгенерировать черновик ответа.

Важно: этот скрипт НИКОГДА не печатает и не кликает ничего в самой странице
чата — только читает текст (`.all_text_contents()`). В коде намеренно нет
функции отправки: печатает и отправляет ответ всегда человек, вручную,
в панели /draft (см. web/static/draft.html) он читает готовый черновик,
копирует и вставляет сам.

Перед запуском обязательно заполните:
  1. CHAT_URL — адрес страницы с чатом.
  2. INCOMING_SELECTOR — CSS-селектор ТОЛЬКО входящих сообщений (не ваших
     собственных исходящих). Найти: открыть чат в браузере, ПКМ на
     сообщении собеседника -> "Просмотреть код" (Inspect), найти класс,
     который есть у входящих сообщений и которого нет у исходящих.

Установка (один раз):
    pip install -r requirements.txt
    playwright install chromium

Запуск:
    python -m agent.watcher
Отдельным терминалом должен быть поднят backend:
    uvicorn web.server:app
"""
from __future__ import annotations

import time

import requests
from playwright.sync_api import sync_playwright

CHAT_URL = "https://example.invalid/chat"  # TODO: реальный адрес чата
USER_DATA_DIR = "./.pw-profile"  # логин-сессия сохраняется тут между запусками

INCOMING_SELECTOR = ".message--incoming"  # TODO: реальный селектор входящих сообщений
POLL_INTERVAL_SECONDS = 3

DRAFT_API_URL = "http://127.0.0.1:8000/api/draft"


def watch() -> None:
    with sync_playwright() as pw:
        context = pw.chromium.launch_persistent_context(USER_DATA_DIR, headless=False)
        page = context.new_page()
        page.goto(CHAT_URL)
        input("Залогиньтесь в открывшемся окне, откройте нужный чат, затем нажмите Enter здесь... ")

        last_seen: str | None = None
        print("Слежу за новыми сообщениями (Ctrl+C для выхода)...")

        while True:
            try:
                messages = page.locator(INCOMING_SELECTOR).all_text_contents()
            except Exception as exc:
                print(f"Не удалось прочитать страницу: {exc}")
                messages = []

            latest = messages[-1].strip() if messages else None

            if latest and latest != last_seen:
                last_seen = latest
                print(f"Новое сообщение: {latest[:80]!r} -> запрашиваю черновик...")
                try:
                    requests.post(DRAFT_API_URL, json={"message": latest}, timeout=120)
                except requests.RequestException as exc:
                    print(f"Backend недоступен: {exc}")

            time.sleep(POLL_INTERVAL_SECONDS)


if __name__ == "__main__":
    watch()
