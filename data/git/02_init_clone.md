# Git: создать репозиторий или склонировать

```bash
git init                      # превратить текущую папку в репозиторий
git init my-project           # создать новую папку с репозиторием

git clone https://github.com/user/repo.git
git clone git@github.com:user/repo.git      # по SSH
git clone URL my-folder                     # в папку с другим именем
git clone --depth 1 URL                     # только последний коммит (быстро)
```

После `git init` нужно добавить удалённый репозиторий, чтобы делать push:
`git remote add origin URL`, затем `git push -u origin main`.
