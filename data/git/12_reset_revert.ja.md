# Git：コミットの取り消し — reset と revert

```bash
git reset --soft HEAD~1    # コミットを取り消し、変更はインデックスに残す
git reset HEAD~1           # （--mixed）変更はファイルに残し、インデックスからは外す
git reset --hard HEAD~1    # コミットとその変更をすべて削除
git revert abc1234         # abc1234 を打ち消す新しいコミットを作る
```

すでに共有ブランチに push したコミットは `git revert` を使います。履歴を書き換えないので、ほかの人にとって安全です。

`reset` はまだ送信していないローカルのコミット向けです。`reset --hard` はコミットしていない変更も消します。誤って失ったコミットは、たいてい `git reflog` で見つけられます。
