from __future__ import annotations

import numpy as np

from . import config

_model = None


def _get_model():
    global _model
    if _model is None:
        from sentence_transformers import SentenceTransformer

        _model = SentenceTransformer(config.EMBEDDING_MODEL_NAME, device="cpu")
    return _model


def embed_passages(texts: list[str]) -> np.ndarray:
    model = _get_model()
    prefixed = [f"passage: {t}" for t in texts]
    vectors = model.encode(prefixed, normalize_embeddings=True, show_progress_bar=False)
    return np.asarray(vectors, dtype=np.float32)


def embed_query(text: str) -> np.ndarray:
    model = _get_model()
    vector = model.encode([f"query: {text}"], normalize_embeddings=True, show_progress_bar=False)
    return np.asarray(vector, dtype=np.float32)[0]
