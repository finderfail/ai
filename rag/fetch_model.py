from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import requests

from . import config
from .encoder import MODEL_FILES, BertEncoder, is_model_dir

CHUNK = 1 << 20


def download(url: str, target: Path) -> None:
    tmp = target.with_name(target.name + ".part")
    with requests.get(url, stream=True, timeout=60, allow_redirects=True) as resp:
        resp.raise_for_status()
        total = int(resp.headers.get("content-length") or 0)
        done = 0
        with open(tmp, "wb") as handle:
            for block in resp.iter_content(CHUNK):
                handle.write(block)
                done += len(block)
                if total:
                    sys.stdout.write(f"\r  {target.name}: {done >> 20}/{total >> 20} МБ")
                    sys.stdout.flush()
    if total and done != total:
        tmp.unlink(missing_ok=True)
        raise SystemExit(f"\n{target.name}: скачано {done} из {total} байт, попробуйте ещё раз")
    os.replace(tmp, target)
    sys.stdout.write(f"\r  {target.name}: готово, {done >> 20} МБ\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Один раз скачивает модель эмбеддингов в папку проекта")
    parser.add_argument("--target", default=str(config.EMBEDDING_LOCAL_DIR))
    parser.add_argument("--revision", default="main")
    args = parser.parse_args()

    target = Path(args.target).expanduser()
    if is_model_dir(target):
        print(f"Модель уже есть в {target}")
    else:
        target.mkdir(parents=True, exist_ok=True)
        endpoint = os.getenv("HF_ENDPOINT", "https://huggingface.co").rstrip("/")
        print(f"Скачиваю {config.EMBEDDING_MODEL_NAME} с {endpoint} в {target}")
        for name in MODEL_FILES:
            if (target / name).exists():
                continue
            try:
                download(f"{endpoint}/{config.EMBEDDING_MODEL_NAME}/resolve/{args.revision}/{name}", target / name)
            except requests.RequestException as exc:
                raise SystemExit(
                    f"\nНе удалось скачать {name}: {exc}\n"
                    "Можно указать зеркало (HF_ENDPOINT=https://hf-mirror.com) "
                    "или скопировать папку с моделью с другой машины и указать её в EMBEDDING_MODEL_DIR"
                )

    BertEncoder(target).encode(["query: проверка"])
    print("Модель загружается и считает эмбеддинги")


if __name__ == "__main__":
    main()
