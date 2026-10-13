# Git: ветки

```bash
git branch                     # список локальных веток
git branch -a                  # включая удалённые
git switch -c feature/login    # создать ветку и перейти на неё
git switch main                # перейти на ветку
git branch -d feature/login    # удалить слитую ветку
git branch -D feature/login    # удалить принудительно
git branch -m new-name         # переименовать текущую ветку
git push -u origin feature/login   # опубликовать ветку
git push origin --delete feature/login   # удалить на сервере
```

`git checkout -b имя` — старый эквивалент `git switch -c имя`. Перед переключением веток закоммитьте или спрячьте (`git stash`) незавершённые изменения.
