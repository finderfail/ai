# Git: первоначальная настройка

```bash
git config --global user.name "Имя Фамилия"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global core.editor "nano"     # редактор для сообщений коммитов
git config --global pull.rebase false      # поведение git pull: merge
git config --list --show-origin            # посмотреть все настройки и откуда они
git --version
```

`--global` пишет в `~/.gitconfig` для всех репозиториев. Без флага настройка применяется только к текущему репозиторию (`.git/config`) — удобно, чтобы для рабочего проекта указать рабочую почту.
