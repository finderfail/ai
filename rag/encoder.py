from __future__ import annotations

import json
import os
import struct
from pathlib import Path

import numpy as np
from tokenizers import Tokenizer

DTYPES = {"F32": np.float32, "F16": np.float16, "I64": np.int64}


MODEL_FILES = ("config.json", "tokenizer.json", "model.safetensors")


def is_model_dir(path: Path) -> bool:
    return all((path / name).exists() for name in MODEL_FILES)


def resolve_model_dir(name: str, override: str | None = None, local: Path | None = None) -> Path:
    if override:
        path = Path(override).expanduser()
        if is_model_dir(path):
            return path
        raise FileNotFoundError(f"В {path} нет файлов модели эмбеддингов: {', '.join(MODEL_FILES)}")
    if local is not None and is_model_dir(local):
        return local
    hub = os.getenv("HF_HUB_CACHE") or os.path.join(
        os.getenv("HF_HOME", os.path.expanduser("~/.cache/huggingface")), "hub"
    )
    repo = Path(hub) / ("models--" + name.replace("/", "--"))
    ref = repo / "refs" / "main"
    if ref.exists():
        snapshot = repo / "snapshots" / ref.read_text().strip()
        if is_model_dir(snapshot):
            return snapshot
    snapshots = sorted(p.parent for p in repo.glob("snapshots/*/config.json")) if repo.exists() else []
    for snapshot in reversed(snapshots):
        if is_model_dir(snapshot):
            return snapshot
    raise FileNotFoundError(
        f"Модель эмбеддингов {name} не найдена ни в {local}, ни в {hub}. "
        "Скачайте её один раз: python -m rag.fetch_model"
    )


def _open_safetensors(path: Path) -> dict[str, np.ndarray]:
    with open(path, "rb") as handle:
        header_size = struct.unpack("<Q", handle.read(8))[0]
        header = json.loads(handle.read(header_size))
    raw = np.memmap(path, dtype=np.uint8, mode="r")
    base = 8 + header_size
    tensors = {}
    for name, info in header.items():
        if name == "__metadata__":
            continue
        start, end = info["data_offsets"]
        dtype = DTYPES[info["dtype"]]
        tensors[name] = raw[base + start : base + end].view(dtype).reshape(info["shape"])
    return tensors


def _erf(x: np.ndarray) -> np.ndarray:
    sign = np.sign(x)
    x = np.abs(x)
    t = 1.0 / (1.0 + 0.3275911 * x)
    poly = t * (0.254829592 + t * (-0.284496736 + t * (1.421413741 + t * (-1.453152027 + t * 1.061405429))))
    return sign * (1.0 - poly * np.exp(-x * x))


def _gelu(x: np.ndarray) -> np.ndarray:
    return 0.5 * x * (1.0 + _erf(x * np.float32(0.7071067811865476)))


def _layer_norm(x: np.ndarray, weight: np.ndarray, bias: np.ndarray, eps: float) -> np.ndarray:
    mean = x.mean(-1, keepdims=True)
    var = ((x - mean) ** 2).mean(-1, keepdims=True)
    return (x - mean) / np.sqrt(var + eps) * weight + bias


class BertEncoder:
    def __init__(self, model_dir: Path, max_length: int = 512):
        config = json.loads((model_dir / "config.json").read_text())
        if config.get("model_type") != "bert":
            raise ValueError(f"Поддерживаются только BERT-модели, а не {config.get('model_type')}")
        self.hidden = config["hidden_size"]
        self.heads = config["num_attention_heads"]
        self.head_dim = self.hidden // self.heads
        self.eps = config.get("layer_norm_eps", 1e-12)
        self.max_length = min(max_length, config["max_position_embeddings"])

        self.tokenizer = Tokenizer.from_file(str(model_dir / "tokenizer.json"))
        self.tokenizer.enable_truncation(self.max_length)
        self.tokenizer.no_padding()

        weights = _open_safetensors(model_dir / "model.safetensors")
        prefix = "bert." if "bert.embeddings.word_embeddings.weight" in weights else ""

        def take(name: str) -> np.ndarray:
            return np.ascontiguousarray(weights[prefix + name], dtype=np.float32)

        self.word = weights[prefix + "embeddings.word_embeddings.weight"]
        self.position = take("embeddings.position_embeddings.weight")
        self.token_type = take("embeddings.token_type_embeddings.weight")[0]
        self.emb_norm = (take("embeddings.LayerNorm.weight"), take("embeddings.LayerNorm.bias"))

        self.layers = []
        for i in range(config["num_hidden_layers"]):
            p = f"encoder.layer.{i}."
            qkv_w = np.concatenate(
                [take(p + f"attention.self.{n}.weight") for n in ("query", "key", "value")]
            ).T.copy()
            qkv_b = np.concatenate([take(p + f"attention.self.{n}.bias") for n in ("query", "key", "value")])
            self.layers.append(
                (
                    qkv_w,
                    qkv_b,
                    take(p + "attention.output.dense.weight").T.copy(),
                    take(p + "attention.output.dense.bias"),
                    take(p + "attention.output.LayerNorm.weight"),
                    take(p + "attention.output.LayerNorm.bias"),
                    take(p + "intermediate.dense.weight").T.copy(),
                    take(p + "intermediate.dense.bias"),
                    take(p + "output.dense.weight").T.copy(),
                    take(p + "output.dense.bias"),
                    take(p + "output.LayerNorm.weight"),
                    take(p + "output.LayerNorm.bias"),
                )
            )

    def _forward(self, ids: np.ndarray, mask: np.ndarray) -> np.ndarray:
        batch, length = ids.shape
        x = np.asarray(self.word[ids], dtype=np.float32) + self.position[:length] + self.token_type
        x = _layer_norm(x, *self.emb_norm, self.eps)
        bias = np.where(mask[:, None, None, :] > 0, 0.0, -1e9).astype(np.float32)
        scale = np.float32(1.0 / np.sqrt(self.head_dim))

        for qkv_w, qkv_b, o_w, o_b, n1_w, n1_b, i_w, i_b, f_w, f_b, n2_w, n2_b in self.layers:
            qkv = (x @ qkv_w + qkv_b).reshape(batch, length, 3, self.heads, self.head_dim)
            q, k, v = (qkv[:, :, j].transpose(0, 2, 1, 3) for j in range(3))
            scores = (q @ k.transpose(0, 1, 3, 2)) * scale + bias
            scores -= scores.max(-1, keepdims=True)
            probs = np.exp(scores)
            probs /= probs.sum(-1, keepdims=True)
            context = (probs @ v).transpose(0, 2, 1, 3).reshape(batch, length, self.hidden)
            x = _layer_norm(x + context @ o_w + o_b, n1_w, n1_b, self.eps)
            x = _layer_norm(x + _gelu(x @ i_w + i_b) @ f_w + f_b, n2_w, n2_b, self.eps)

        weights = mask[:, :, None].astype(np.float32)
        pooled = (x * weights).sum(1) / np.maximum(weights.sum(1), 1e-9)
        return pooled / np.maximum(np.linalg.norm(pooled, axis=1, keepdims=True), 1e-12)

    def encode(self, texts: list[str], batch_size: int = 16, on_batch=None) -> np.ndarray:
        encodings = self.tokenizer.encode_batch(texts)
        order = sorted(range(len(texts)), key=lambda i: len(encodings[i].ids))
        result = np.zeros((len(texts), self.hidden), dtype=np.float32)
        for start in range(0, len(order), batch_size):
            group = order[start : start + batch_size]
            length = max(len(encodings[i].ids) for i in group)
            ids = np.zeros((len(group), length), dtype=np.int64)
            mask = np.zeros((len(group), length), dtype=np.int64)
            for row, i in enumerate(group):
                seq = encodings[i].ids
                ids[row, : len(seq)] = seq
                mask[row, : len(seq)] = 1
            result[group] = self._forward(ids, mask)
            if on_batch is not None:
                on_batch(len(group))
        return result
