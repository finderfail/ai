# Git：.gitignore

リポジトリのルートにある `.gitignore` には、git に追跡させないものを書きます。

```
node_modules/
.venv/
__pycache__/
*.log
.env
dist/
.DS_Store
!keep.log
```

末尾の `/` はディレクトリのみ、`*` は任意の文字列、`!` はルールの例外です。

`.gitignore` はすでに追跡中のファイルには効きません。ファイルをディスクに残したまま追跡をやめるには `git rm --cached .env` してコミットします。どのルールで無視されているかの確認：`git check-ignore -v パス`。
