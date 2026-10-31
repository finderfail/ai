from __future__ import annotations

import sys
import time

import numpy as np

from . import config
from .embeddings import embed_passages
from .lexical import LexicalIndex
from .store import Chunk, VectorStore, digest


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


def build_index(force: bool = False) -> None:
    started = time.perf_counter()
    hints = collect_hints()

    previous: dict = {}
    if not force:
        meta, previous = VectorStore.read_vectors()
        if meta.get("embedding_model") != config.EMBEDDING_MODEL_NAME:
            previous = {}

    vectors: list[np.ndarray | None] = []
    pending: list[int] = []
    for i, hint in enumerate(hints):
        vector = previous.get((hint.domain, hint.source, digest(hint.text)))
        vectors.append(vector)
        if vector is None:
            pending.append(i)

    if pending:
        print(f"Файлов: {len(hints)}. Новых или изменённых: {len(pending)}. Считаю эмбеддинги...")
        fresh = embed_passages([hints[i].text for i in pending], show_progress=True)
        for row, i in enumerate(pending):
            vectors[i] = fresh[row]

    print("Строю лексический индекс...")
    lexical = LexicalIndex.build([hint.text for hint in hints])

    matrix = np.vstack(vectors).astype(np.float32)
    VectorStore(matrix, hints, lexical).save(
        {
            "embedding_model": config.EMBEDDING_MODEL_NAME,
            "documents": str(len(hints)),
            "built_at": str(time.time()),
        }
    )
    print(
        f"Индекс сохранён в {config.INDEX_DB_PATH}: переиспользовано {len(hints) - len(pending)}, "
        f"пересчитано {len(pending)}, {time.perf_counter() - started:.1f} с"
    )


if __name__ == "__main__":
    build_index(force="--force" in sys.argv[1:])
