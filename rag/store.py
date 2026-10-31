from __future__ import annotations

import hashlib
import os
import re
import sqlite3
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from . import config
from .lexical import LexicalIndex

NON_WORD_RE = re.compile(r"[\W_]+")

SCHEMA = """
CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE chunks (
    id INTEGER PRIMARY KEY,
    domain TEXT NOT NULL,
    source TEXT NOT NULL,
    text TEXT NOT NULL,
    digest TEXT NOT NULL,
    vector BLOB NOT NULL
);
CREATE INDEX chunks_source ON chunks (domain, source);
CREATE TABLE postings (
    term TEXT NOT NULL,
    doc INTEGER NOT NULL,
    tf INTEGER NOT NULL,
    PRIMARY KEY (term, doc)
) WITHOUT ROWID;
"""


def flatten(text: str) -> str:
    return NON_WORD_RE.sub(" ", text.lower().replace("ё", "е")).strip()


def digest(text: str) -> str:
    return hashlib.blake2b(text.encode("utf-8"), digest_size=16).hexdigest()


@dataclass
class Chunk:
    id: int
    text: str
    source: str
    domain: str


class VectorStore:
    def __init__(
        self,
        embeddings: np.ndarray,
        chunks: list[Chunk],
        lexical: LexicalIndex | None = None,
        version: float = 0.0,
    ):
        self.embeddings = embeddings
        self.chunks = chunks
        self.lexical = lexical
        self.version = version
        self.lowered_texts = [flatten(c.text) for c in chunks]
        self.domains = np.array([c.domain for c in chunks])
        self._domain_masks: dict[frozenset[str], np.ndarray] = {}

    def save(self, meta: dict[str, str], path: Path = config.INDEX_DB_PATH) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(".db.tmp")
        tmp.unlink(missing_ok=True)
        conn = sqlite3.connect(tmp)
        try:
            conn.executescript(SCHEMA)
            conn.executemany("INSERT INTO meta VALUES (?, ?)", list(meta.items()))
            conn.executemany(
                "INSERT INTO chunks VALUES (?, ?, ?, ?, ?, ?)",
                (
                    (c.id, c.domain, c.source, c.text, digest(c.text), self.embeddings[c.id].tobytes())
                    for c in self.chunks
                ),
            )
            if self.lexical is not None:
                conn.executemany(
                    "INSERT INTO postings VALUES (?, ?, ?)",
                    (
                        (term, doc, tf)
                        for doc, counts in enumerate(self.lexical.doc_tokens)
                        for term, tf in counts.items()
                    ),
                )
            conn.commit()
        finally:
            conn.close()
        os.replace(tmp, path)

    @staticmethod
    def read_vectors(path: Path = config.INDEX_DB_PATH) -> tuple[dict[str, str], dict[tuple[str, str, str], np.ndarray]]:
        if not path.exists():
            return {}, {}
        conn = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
        try:
            meta = dict(conn.execute("SELECT key, value FROM meta"))
            rows = conn.execute("SELECT domain, source, digest, vector FROM chunks")
            vectors = {(d, s, h): np.frombuffer(v, dtype=np.float32) for d, s, h, v in rows}
        finally:
            conn.close()
        return meta, vectors

    @classmethod
    def load(cls, path: Path = config.INDEX_DB_PATH) -> "VectorStore":
        if not path.exists():
            raise FileNotFoundError("Индекс не найден. Сначала запустите: python -m rag.ingest")
        version = path.stat().st_mtime
        conn = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
        try:
            rows = conn.execute("SELECT id, domain, source, text, vector FROM chunks ORDER BY id").fetchall()
            postings = conn.execute("SELECT doc, term, tf FROM postings").fetchall()
        finally:
            conn.close()
        chunks = [Chunk(id=i, text=text, source=source, domain=domain) for i, domain, source, text, _ in rows]
        embeddings = (
            np.frombuffer(b"".join(r[4] for r in rows), dtype=np.float32).reshape(len(rows), -1)
            if rows
            else np.zeros((0, 0), dtype=np.float32)
        )
        lexical = LexicalIndex.from_postings(len(chunks), postings) if postings else None
        return cls(embeddings, chunks, lexical, version)

    def domain_mask(self, domains: set[str]) -> np.ndarray:
        key = frozenset(domains)
        mask = self._domain_masks.get(key)
        if mask is None:
            mask = np.isin(self.domains, list(key))
            self._domain_masks[key] = mask
        return mask

    def search(
        self,
        query_vector: np.ndarray,
        top_k: int | None = None,
        domains: set[str] | None = None,
        scores: np.ndarray | None = None,
    ) -> list[tuple[Chunk, float]]:
        if scores is None:
            scores = self.embeddings @ query_vector
        candidate_idx = (
            np.flatnonzero(self.domain_mask(domains)) if domains is not None else np.arange(len(self.chunks))
        )
        if candidate_idx.size == 0:
            return []
        candidate_scores = scores[candidate_idx]
        order = np.argsort(-candidate_scores)
        if top_k is not None:
            order = order[:top_k]
        return [(self.chunks[candidate_idx[i]], float(candidate_scores[i])) for i in order]
