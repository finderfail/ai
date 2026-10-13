# Git：変更の一時退避 — stash

```bash
git stash                    # コミットしていない変更を退避
git stash -u                 # 未追跡ファイルも含めて退避
git stash push -m "wip: ログインフォーム"
git stash list               # 退避した一覧
git stash pop                # 最新を戻して一覧から削除
git stash apply stash@{1}    # 指定したものを削除せずに適用
git stash drop stash@{1}     # 項目を削除
git stash show -p stash@{0}  # 内容を確認
```

典型例：作業がまだコミットできない状態で急に別ブランチに切り替える必要があるとき — `git stash`、`git switch hotfix`、…、戻って `git stash pop`。
