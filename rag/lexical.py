from __future__ import annotations

import math
import re
from dataclasses import dataclass

TOKEN_RE = re.compile(r"[a-zA-Zа-яА-ЯёЁ0-9]+|[\u3040-\u30ff\u3400-\u9fff\uff66-\uff9f]+")
CJK_RE = re.compile(r"[\u3040-\u30ff\u3400-\u9fff\uff66-\uff9f]")

RU_SUFFIXES = (
    "иями", "ами", "ями", "ого", "его", "ому", "ему", "ыми", "ими", "ость",
    "ать", "ять", "ить", "еть", "ов", "ев", "ий", "ый", "ая", "яя", "ое", "ее",
    "ые", "ие", "ую", "юю", "ом", "ем", "ах", "ях", "ью", "ии", "ия", "ам", "ям", "ой", "ей",
    "а", "я", "о", "е", "ы", "и", "у", "ю", "ь", "й",
)

EN_SUFFIXES = ("ing", "ed", "es", "s")

MIN_STEM = 4


def stem(word: str) -> str:
    if len(word) <= MIN_STEM:
        return word
    for suffix in RU_SUFFIXES:
        if word.endswith(suffix) and len(word) - len(suffix) >= MIN_STEM:
            return word[: -len(suffix)]
    for suffix in EN_SUFFIXES:
        if word.endswith(suffix) and len(word) - len(suffix) >= MIN_STEM:
            return word[: -len(suffix)]
    return word


def cjk_bigrams(run: str) -> list[str]:
    if len(run) == 1:
        return [run]
    return [run[i : i + 2] for i in range(len(run) - 1)]


def tokenize(text: str) -> list[str]:
    tokens: list[str] = []
    for match in TOKEN_RE.findall(text.replace("ё", "е").replace("Ё", "Е")):
        if CJK_RE.match(match):
            tokens.extend(cjk_bigrams(match))
        elif len(match) >= 2:
            tokens.append(stem(match.lower()))
    return tokens


@dataclass
class LexicalIndex:
    doc_tokens: list[dict[str, int]]
    doc_lengths: list[int]
    idf: dict[str, float]
    avg_length: float

    def to_dict(self) -> dict:
        return {
            "doc_tokens": self.doc_tokens,
            "doc_lengths": self.doc_lengths,
            "idf": self.idf,
            "avg_length": self.avg_length,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "LexicalIndex":
        return cls(
            doc_tokens=data["doc_tokens"],
            doc_lengths=data["doc_lengths"],
            idf=data["idf"],
            avg_length=data["avg_length"],
        )

    @classmethod
    def build(cls, texts: list[str]) -> "LexicalIndex":
        doc_tokens: list[dict[str, int]] = []
        doc_lengths: list[int] = []
        doc_freq: dict[str, int] = {}

        for text in texts:
            tokens = tokenize(text)
            counts: dict[str, int] = {}
            for token in tokens:
                counts[token] = counts.get(token, 0) + 1
            doc_tokens.append(counts)
            doc_lengths.append(len(tokens))
            for token in counts:
                doc_freq[token] = doc_freq.get(token, 0) + 1

        total = len(texts)
        idf = {
            token: math.log(1 + (total - df + 0.5) / (df + 0.5))
            for token, df in doc_freq.items()
        }
        avg_length = sum(doc_lengths) / total if total else 0.0
        return cls(doc_tokens, doc_lengths, idf, avg_length)

    def unseen_idf(self) -> float:
        total = len(self.doc_tokens)
        return math.log(1 + (total + 0.5) / 0.5)

    def query_coverage(self, query: str, doc_index: int) -> float:
        query_tokens = set(tokenize(query))
        if not query_tokens:
            return 0.0

        fallback = self.unseen_idf()
        total_mass = 0.0
        matched_mass = 0.0
        doc = self.doc_tokens[doc_index]

        for token in query_tokens:
            weight = self.idf.get(token, fallback)
            total_mass += weight
            if token in doc:
                matched_mass += weight

        return matched_mass / total_mass if total_mass else 0.0

    def bm25(self, query: str, doc_index: int, k1: float = 1.5, b: float = 0.75) -> float:
        doc = self.doc_tokens[doc_index]
        length = self.doc_lengths[doc_index]
        score = 0.0
        for token in tokenize(query):
            freq = doc.get(token)
            if not freq:
                continue
            weight = self.idf.get(token, 0.0)
            denom = freq + k1 * (1 - b + b * length / self.avg_length) if self.avg_length else freq
            score += weight * (freq * (k1 + 1)) / denom if denom else 0.0
        return score
