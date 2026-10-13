# Git: слияние веток merge

```bash
git switch main
git pull                     # обновить main
git merge feature/login      # влить ветку в main
git merge --no-ff feature/login   # всегда создавать merge-коммит
git merge --abort            # отменить слияние при конфликте
```

Если main не уходил вперёд, git делает fast-forward — просто передвигает указатель без отдельного коммита. Флаг `--no-ff` сохраняет в истории явную точку слияния.

После успешного слияния ветку можно удалить: `git branch -d feature/login`.
