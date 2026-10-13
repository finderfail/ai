from __future__ import annotations

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


def build_index() -> None:
    hints = collect_hints()

    print(f"Найдено {len(hints)} файлов-подсказок. Считаю эмбеддинги...")
    texts = [h.text for h in hints]
    vectors = embed_passages(texts)

    print("Строю лексический индекс...")
    lexical = LexicalIndex.build(texts)

    VectorStore(vectors, hints, lexical).save()
    print(f"Индекс сохранён в {config.INDEX_DIR}")


if __name__ == "__main__":
    build_index()
