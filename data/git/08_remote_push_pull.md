# Git: удалённые репозитории — fetch, pull, push

```bash
git remote -v                       # список удалённых репозиториев
git remote add origin URL           # добавить
git remote set-url origin NEW_URL   # сменить адрес
git fetch                           # скачать изменения, не трогая ваши ветки
git pull                            # fetch + merge в текущую ветку
git pull --rebase                   # fetch + rebase (линейная история)
git push                            # отправить текущую ветку
git push -u origin main             # первый push с привязкой ветки
```

Ошибка `rejected (fetch first)` / `non-fast-forward` значит, что на сервере есть коммиты, которых нет у вас: сделайте `git pull`, решите конфликты и повторите `git push`.
