# Git：ブランチのマージ

```bash
git switch main
git pull                     # main を最新にする
git merge feature/login      # ブランチを main に取り込む
git merge --no-ff feature/login   # 常にマージコミットを作る
git merge --abort            # コンフリクト時にマージを中止
```

main が先に進んでいなければ fast-forward となり、マージコミットを作らずに参照を進めるだけです。`--no-ff` を付けると、履歴にマージの地点が明示的に残ります。

マージに成功したらブランチを削除できます：`git branch -d feature/login`。
