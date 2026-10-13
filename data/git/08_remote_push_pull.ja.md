# Git：リモート — fetch・pull・push

```bash
git remote -v                       # リモート一覧
git remote add origin URL           # 追加
git remote set-url origin NEW_URL   # URL を変更
git fetch                           # 変更を取得（自分のブランチは変えない）
git pull                            # fetch + 現在のブランチへ merge
git pull --rebase                   # fetch + rebase（直線的な履歴）
git push                            # 現在のブランチを送信
git push -u origin main             # 初回 push とブランチの紐付け
```

`rejected (fetch first)` や `non-fast-forward` は、サーバーに自分の持っていないコミットがあるという意味です。`git pull` してコンフリクトを解決し、もう一度 `git push` します。
