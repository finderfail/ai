from __future__ import annotations

import json
import re
from dataclasses import dataclass

import numpy as np

from . import config
from .lexical import LexicalIndex


TRANSLATION_SUFFIX = ".ja.md"
NON_WORD_RE = re.compile(r"[\W_]+")


def flatten(text: str) -> str:
    return NON_WORD_RE.sub(" ", text.lower().replace("ё", "е")).strip()



@dataclass
class Chunk:
    id: int
    text: str
    source: str
    domain: str

    @property
    def language(self) -> str:
        return "ja" if self.source.endswith(TRANSLATION_SUFFIX) else "ru"

    @property
    def base_key(self) -> tuple[str, str]:
        name = self.source
        if name.endswith(TRANSLATION_SUFFIX):
            name = name[: -len(TRANSLATION_SUFFIX)]
        elif name.endswith(".md"):
            name = name[:-3]
        return self.domain, name


class VectorStore:
    def __init__(
        self,
        embeddings: np.ndarray,
        chunks: list[Chunk],
        lexical: LexicalIndex | None = None,
    ):
        self.embeddings = embeddings
        self.chunks = chunks
        self.lexical = lexical
        self.variants = {(c.base_key, c.language): c for c in chunks}
        self.lowered_texts = [flatten(c.text) for c in chunks]

    def variant(self, chunk: Chunk, language: str) -> Chunk:
        return self.variants.get((chunk.base_key, language), chunk)

    def save(self) -> None:
        config.INDEX_DIR.mkdir(parents=True, exist_ok=True)
        np.save(config.INDEX_EMBEDDINGS_PATH, self.embeddings)
        payload = [
            {"id": c.id, "text": c.text, "source": c.source, "domain": c.domain}
            for c in self.chunks
        ]
        config.INDEX_CHUNKS_PATH.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        if self.lexical is not None:
            config.INDEX_LEXICAL_PATH.write_text(
                json.dumps(self.lexical.to_dict(), ensure_ascii=False), encoding="utf-8"
            )

    @classmethod
    def load(cls) -> "VectorStore":
        if not config.INDEX_EMBEDDINGS_PATH.exists() or not config.INDEX_CHUNKS_PATH.exists():
            raise FileNotFoundError(
                "Индекс не найден. Сначала запустите: python -m rag.ingest"
            )
        embeddings = np.load(config.INDEX_EMBEDDINGS_PATH)
        raw = json.loads(config.INDEX_CHUNKS_PATH.read_text(encoding="utf-8"))
        chunks = [
            Chunk(id=r["id"], text=r["text"], source=r["source"], domain=r["domain"])
            for r in raw
        ]
        lexical = None
        if config.INDEX_LEXICAL_PATH.exists():
            lexical = LexicalIndex.from_dict(
                json.loads(config.INDEX_LEXICAL_PATH.read_text(encoding="utf-8"))
            )
        return cls(embeddings, chunks, lexical)

    def search(
        self,
        query_vector: np.ndarray,
        top_k: int | None = None,
        domains: set[str] | None = None,
    ) -> list[tuple[Chunk, float]]:
        candidate_idx = range(len(self.chunks))
        if domains is not None:
            candidate_idx = [i for i in candidate_idx if self.chunks[i].domain in domains]
        if not candidate_idx:
            return []
        candidate_idx = np.array(list(candidate_idx))
        candidate_scores = self.embeddings[candidate_idx] @ query_vector
        order = np.argsort(-candidate_scores)
        if top_k is not None:
            order = order[:top_k]
        return [(self.chunks[candidate_idx[i]], float(candidate_scores[i])) for i in order]
