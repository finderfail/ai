# Git：初期設定

```bash
git config --global user.name "山田 太郎"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global core.editor "nano"     # コミットメッセージ用エディタ
git config --global pull.rebase false      # git pull の動作：merge
git config --list --show-origin            # すべての設定とその出所
git --version
```

`--global` は `~/.gitconfig` に書かれ、全リポジトリに適用されます。フラグなしだと現在のリポジトリ（`.git/config`）だけに適用されるので、仕事用のプロジェクトに仕事用のメールを設定するのに便利です。
