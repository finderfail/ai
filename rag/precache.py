from __future__ import annotations

import argparse
import time

import requests

from . import answer_cache, config
from .llm import check_ollama_available
from .pipeline import answer_stream, is_cross_lingual

MAX_FAILURES_IN_ROW = 3


def read_questions() -> list[str]:
    path = config.PRECACHE_QUESTIONS_PATH
    if not path.exists():
        return []
    lines = (line.strip() for line in path.read_text(encoding="utf-8").splitlines())
    return [line for line in lines if line and not line.startswith("#")]


def domain_sets(model_id: str) -> list[set[str]]:
    full = config.RAG_DOMAINS | config.GOVERNANCE_DOMAINS
    if config.MODELS[model_id]["governance_only"]:
        return [full]
    return [set(config.RAG_DOMAINS), full] if config.GOVERNANCE_DOMAINS else [set(config.RAG_DOMAINS)]


def run(models: list[str], questions: list[tuple[str, str]]) -> None:
    answer_cache.origin = "precache"
    total = len(models) * len(questions)
    done = cached = failed = empty = in_row = 0
    started = time.perf_counter()
    for model_id in models:
        request = config.model_request(model_id, None)
        for question, language in questions:
            done += 1
            for domains in domain_sets(model_id):
                usage: dict = {}
                t0 = time.perf_counter()
                try:
                    _, stream = answer_stream(question, usage=usage, language=language, domains=domains, **request)
                    if usage.get("cached"):
                        cached += 1
                        for _ in stream:
                            pass
                        continue
                    text = "".join(stream)
                except requests.RequestException as exc:
                    failed += 1
                    in_row += 1
                    print(f"[{done}/{total}] {model_id} {language} ошибка модели: {exc}")
                    if in_row >= MAX_FAILURES_IN_ROW:
                        raise SystemExit(
                            f"{MAX_FAILURES_IN_ROW} ошибки подряд, останавливаюсь. "
                            f"Проверьте OLLAMA_HOST={config.OLLAMA_HOST} в .env"
                        )
                    continue
                in_row = 0
                print(f"[{done}/{total}] {model_id} {language} {time.perf_counter() - t0:5.1f} с  {question[:60]}")
                if not text.strip():
                    empty += 1
    print(
        f"Готово за {time.perf_counter() - started:.0f} с: вопросов {total}, "
        f"уже были в кеше {cached}, пустых ответов {empty}, ошибок {failed}. Записей в кеше: {answer_cache.stats()['entries']}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Заранее считает ответы модели и кладёт их в кеш")
    parser.add_argument("--models", default=",".join(m for m, v in config.MODELS.items() if not v["governance_only"]))
    parser.add_argument("--language", choices=sorted(config.LANGUAGES), help="язык ответа для всех вопросов")
    parser.add_argument("--popular", type=int, default=0, help="добавить N самых частых вопросов из кеша")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    models = [m.strip() for m in args.models.split(",") if m.strip()]
    unknown = [m for m in models if m not in config.MODELS]
    if unknown:
        raise SystemExit(f"Нет таких моделей: {', '.join(unknown)}. Есть: {', '.join(config.MODELS)}")

    seen: set[tuple[str, str]] = set()
    questions: list[tuple[str, str]] = []
    candidates = [(q, args.language or ("ja" if is_cross_lingual(q) else "ru")) for q in read_questions()]
    candidates += [(q, lang) for q, _, lang in answer_cache.popular(args.popular)] if args.popular else []
    for question, language in candidates:
        key = (answer_cache.question_key(question), language)
        if key[0] and key not in seen:
            seen.add(key)
            questions.append((question, language))
    if args.limit:
        questions = questions[: args.limit]
    if not questions:
        raise SystemExit(f"Нет вопросов. Добавьте их по одному на строку в {config.PRECACHE_QUESTIONS_PATH}")

    if not config.ANSWER_CACHE:
        raise SystemExit("Кеш ответов выключен (ANSWER_CACHE=0)")
    ok, message = check_ollama_available()
    if not ok:
        raise SystemExit(f"{message}\nАдрес берётся из OLLAMA_HOST в {config.ROOT_DIR / '.env'}")
    print(f"Ollama: {config.OLLAMA_HOST}, вопросов: {len(questions)}, модели: {', '.join(models)}")
    run(models, questions)


if __name__ == "__main__":
    main()
