# Git：リポジトリの作成とクローン

```bash
git init                      # 現在のフォルダをリポジトリにする
git init my-project           # 新しいフォルダにリポジトリを作成

git clone https://github.com/user/repo.git
git clone git@github.com:user/repo.git      # SSH で
git clone URL my-folder                     # 別名のフォルダに
git clone --depth 1 URL                     # 最新コミットのみ（高速）
```

`git init` の後に push するには、リモートを追加します：`git remote add origin URL`、続けて `git push -u origin main`。
