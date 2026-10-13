# Git：よくあるエラーとその意味

- `fatal: not a git repository`：リポジトリのフォルダにいません。`cd` で移動するか `git init`。
- `rejected … non-fast-forward`：サーバーに新しいコミットがあります。`git pull` してから `git push`。
- `Your branch is ahead of 'origin/main' by N commits`：未送信のコミットがあります。`git push`。
- `detached HEAD`：ブランチではなくコミットにいます。作業を残すには `git switch -c new-branch`。
- `Permission denied (publickey)`：SSH 鍵が未設定。`ssh-keygen -t ed25519`、公開鍵を GitHub に登録し、`ssh -T git@github.com` で確認。
- `refusing to merge unrelated histories`：共通の履歴がありません。意図どおりなら `git pull --allow-unrelated-histories`。
- `Please commit your changes or stash them`：先に `git commit` か `git stash`。
