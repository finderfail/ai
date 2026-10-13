# Git：ブランチ

```bash
git branch                     # ローカルブランチ一覧
git branch -a                  # リモートも含める
git switch -c feature/login    # 作成して切り替え
git switch main                # ブランチを切り替え
git branch -d feature/login    # マージ済みブランチを削除
git branch -D feature/login    # 強制削除
git branch -m new-name         # 現在のブランチ名を変更
git push -u origin feature/login   # ブランチを公開
git push origin --delete feature/login   # サーバー上で削除
```

`git checkout -b 名前` は `git switch -c 名前` の古い書き方です。ブランチを切り替える前に、作業中の変更はコミットするか退避（`git stash`）してください。
