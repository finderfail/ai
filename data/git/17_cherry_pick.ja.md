# Git：特定のコミットを移す — cherry-pick

```bash
git switch release
git cherry-pick abc1234             # abc1234 を現在のブランチに適用
git cherry-pick abc1234 def5678     # 複数のコミット
git cherry-pick A^..B               # A から B までの範囲
git cherry-pick --continue          # コンフリクト解決後に続行
git cherry-pick --abort
```

ブランチ全体をマージせずに、main のバグ修正だけをリリースブランチに移したいときに便利です。移したコミットには新しいハッシュが付きます。
