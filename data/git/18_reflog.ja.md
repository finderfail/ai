# Git：失ったものの復旧 — reflog

`git reflog` は、`reset --hard`、失敗した rebase、ブランチ削除の後でも、HEAD がどこを指していたかを一定期間（既定で約90日）記録しています。

```bash
git reflog                       # 一覧：HEAD@{0}、HEAD@{1}、…
git reset --hard HEAD@{2}        # ブランチをその状態に戻す
git switch -c rescue abc1234     # 見つけたコミットからブランチを作る
git branch restored abc1234      # 削除したブランチを復元
```

reflog はローカルのみで、ほかのコンピューターやサーバーにはありません。`git restore` や `reset --hard` で消えたコミット前の変更は、reflog でも復元できません。
