from __future__ import annotations

import json
import sys
import time

import numpy as np

from . import config
from .embeddings import embed_passages
from .lexical import LexicalIndex
from .store import Chunk, VectorStore


def collect_hints() -> list[Chunk]:
    hints: list[Chunk] = []
    oversized: list[str] = []

    directories = {**config.DOMAIN_DIRS, **config.GOVERNANCE_DOMAIN_DIRS}
    for domain, directory in directories.items():
        for path in sorted(directory.glob("*.md")):
            text = path.read_text(encoding="utf-8").strip()
            if not text:
                continue
            if len(text) > config.MAX_FILE_CHARS:
                oversized.append(f"  {path.relative_to(config.ROOT_DIR)}: {len(text)} символов")
                continue
            hints.append(Chunk(id=len(hints), text=text, source=path.name, domain=domain))

    if oversized:
        raise SystemExit(
            f"Файлы длиннее {config.MAX_FILE_CHARS} символов, разбейте их на несколько:\n"
            + "\n".join(oversized)
        )
    if not hints:
        raise SystemExit("В data/ и data-governance/ не найдено markdown-файлов")
    return hints


def _load_cache() -> tuple[np.ndarray, list[dict]] | None:
    paths = (config.INDEX_META_PATH, config.INDEX_EMBEDDINGS_PATH, config.INDEX_CHUNKS_PATH)
    if not all(path.exists() for path in paths):
        return None
    try:
        meta = json.loads(config.INDEX_META_PATH.read_text(encoding="utf-8"))
        if meta.get("embedding_model") != config.EMBEDDING_MODEL_NAME:
            return None
        raw = json.loads(config.INDEX_CHUNKS_PATH.read_text(encoding="utf-8"))
        vectors = np.load(config.INDEX_EMBEDDINGS_PATH)
    except (OSError, ValueError, json.JSONDecodeError):
        return None
    if len(raw) != len(vectors) or vectors.ndim != 2:
        return None
    return vectors, raw


def build_index(force: bool = False) -> None:
    started = time.perf_counter()
    hints = collect_hints()
    cached = None if force else _load_cache()

    pending: list[int] = []
    reused = 0
    vectors: np.ndarray | None = None

    if cached is not None:
        previous_vectors, previous_raw = cached
        by_key = {
            (row["domain"], row["source"]): (row["text"], previous_vectors[i])
            for i, row in enumerate(previous_raw)
        }
        vectors = np.empty((len(hints), previous_vectors.shape[1]), dtype=np.float32)
        for i, hint in enumerate(hints):
            entry = by_key.get((hint.domain, hint.source))
            if entry is not None and entry[0] == hint.text:
                vectors[i] = entry[1]
                reused += 1
            else:
                pending.append(i)
    else:
        pending = list(range(len(hints)))

    if pending:
        print(f"Файлов: {len(hints)}. Новых или изменённых: {len(pending)}. Считаю эмбеддинги...")
        fresh = embed_passages([hints[i].text for i in pending], show_progress=True)
        if vectors is None:
            vectors = fresh
        else:
            vectors[pending] = fresh

    if vectors is None:
        raise SystemExit("Не удалось получить эмбеддинги")

    texts = [hint.text for hint in hints]
    print("Строю лексический индекс...")
    lexical = LexicalIndex.build(texts)

    VectorStore(vectors, hints, lexical).save()
    config.INDEX_META_PATH.write_text(
        json.dumps(
            {"embedding_model": config.EMBEDDING_MODEL_NAME, "documents": len(hints)},
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(
        f"Индекс сохранён в {config.INDEX_DIR}: переиспользовано {reused}, "
        f"пересчитано {len(pending)}, {time.perf_counter() - started:.1f} с"
    )


if __name__ == "__main__":
    build_index(force="--force" in sys.argv[1:])
