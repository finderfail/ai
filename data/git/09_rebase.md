# Git: rebase

`git rebase` переносит ваши коммиты поверх другой ветки, делая историю линейной.

```bash
git switch feature
git rebase main              # переложить коммиты feature поверх main
git rebase --continue        # после решения конфликта
git rebase --abort           # вернуть всё как было
git rebase -i HEAD~3         # интерактивно: склеить (squash), переименовать, удалить коммиты
```

Главное правило: не делайте rebase коммитов, которые уже запушены в общую ветку и которыми пользуются другие, — rebase переписывает историю. Для своей личной ветки после rebase нужен `git push --force-with-lease`.
