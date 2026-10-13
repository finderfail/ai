# Bash：アーカイブ tar・gzip・zip

```bash
tar -czf archive.tar.gz dir/        # ディレクトリを .tar.gz に圧縮
tar -xzf archive.tar.gz             # 展開
tar -xzf archive.tar.gz -C /tmp     # /tmp に展開
tar -tzf archive.tar.gz             # 中身の一覧
tar -czf src.tgz --exclude=node_modules src/

gzip file.log          # 圧縮（file.log.gz に置き換わる）
gunzip file.log.gz     # 展開
zip -r site.zip site/  # zip アーカイブ
unzip site.zip -d out/ # zip を展開
```

tar のフラグ：`c` 作成、`x` 展開、`t` 一覧、`z` gzip、`f` ファイル名（名前の直前に置く）。
