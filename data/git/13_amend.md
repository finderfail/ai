# Git: исправить последний коммит

```bash
git commit --amend -m "Новое сообщение"   # поправить сообщение
git add forgotten.py
git commit --amend --no-edit              # добавить забытый файл в тот же коммит
git commit --amend --author="Имя <mail@example.com>" --no-edit
```

`--amend` заменяет последний коммит новым (другой хеш). Если коммит уже запушен, после amend понадобится `git push --force-with-lease`, поэтому в общих ветках так делать не стоит.

Исправить более старый коммит можно через `git rebase -i HEAD~N` и пометку `edit` или `reword`.
