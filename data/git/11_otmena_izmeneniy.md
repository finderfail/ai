# Git: отменить изменения в файлах

```bash
git restore file.py            # отменить правки в рабочей папке (безвозвратно)
git restore --staged file.py   # убрать файл из индекса, правки остаются
git restore --source=HEAD~2 file.py   # вернуть файл к состоянию 2 коммита назад
git clean -n                   # показать неотслеживаемые файлы к удалению
git clean -fd                  # удалить неотслеживаемые файлы и папки
```

Старые эквиваленты: `git checkout -- file.py` вместо `git restore file.py`, `git reset HEAD file.py` вместо `git restore --staged file.py`.

`git restore` и `git clean -f` удаляют несохранённую работу без возможности восстановления — сначала проверьте `git status` и `git clean -n`.
