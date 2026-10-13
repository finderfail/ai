# Bash: архивы tar, gzip, zip

```bash
tar -czf archive.tar.gz dir/        # упаковать каталог в .tar.gz
tar -xzf archive.tar.gz             # распаковать
tar -xzf archive.tar.gz -C /tmp     # распаковать в /tmp
tar -tzf archive.tar.gz             # посмотреть содержимое
tar -czf src.tgz --exclude=node_modules src/

gzip file.log          # сжать (заменит на file.log.gz)
gunzip file.log.gz     # распаковать
zip -r site.zip site/  # zip-архив
unzip site.zip -d out/ # распаковать zip
```

Флаги tar: `c` — создать, `x` — извлечь, `t` — список, `z` — gzip, `f` — имя файла (идёт последним перед именем).
