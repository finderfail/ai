# Git: временно спрятать изменения — stash

```bash
git stash                    # спрятать незакоммиченные изменения
git stash -u                 # вместе с неотслеживаемыми файлами
git stash push -m "wip: форма входа"
git stash list               # список спрятанного
git stash pop                # вернуть последнее и удалить из списка
git stash apply stash@{1}    # применить конкретное, не удаляя
git stash drop stash@{1}     # удалить запись
git stash show -p stash@{0}  # посмотреть содержимое
```

Типичный сценарий: срочно нужно переключиться на другую ветку, а работа не готова к коммиту — `git stash`, `git switch hotfix`, … , вернуться, `git stash pop`.
