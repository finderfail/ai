# Git：rebase

`git rebase` は自分のコミットを別のブランチの上に移し替え、履歴を直線的にします。

```bash
git switch feature
git rebase main              # feature のコミットを main の上に移す
git rebase --continue        # コンフリクト解決後に続行
git rebase --abort           # 元の状態に戻す
git rebase -i HEAD~3         # 対話的に：まとめる（squash）、名前変更、削除
```

大原則：すでに共有ブランチに push され、他の人が使っているコミットを rebase しないこと。rebase は履歴を書き換えます。自分専用のブランチを rebase した後は `git push --force-with-lease` が必要です。
