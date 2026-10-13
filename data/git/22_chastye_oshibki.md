# Git: частые ошибки и что они значат

- `fatal: not a git repository` — вы не в папке репозитория; `cd` в него или `git init`.
- `rejected … non-fast-forward` — на сервере есть новые коммиты: `git pull`, затем `git push`.
- `Your branch is ahead of 'origin/main' by N commits` — есть неотправленные коммиты: `git push`.
- `detached HEAD` — вы на коммите, а не на ветке; чтобы сохранить работу: `git switch -c new-branch`.
- `Permission denied (publickey)` — не настроен SSH-ключ: `ssh-keygen -t ed25519`, добавить публичный ключ в GitHub, проверить `ssh -T git@github.com`.
- `refusing to merge unrelated histories` — у веток нет общей истории; если это ожидаемо: `git pull --allow-unrelated-histories`.
- `Please commit your changes or stash them` — сначала `git commit` или `git stash`.
