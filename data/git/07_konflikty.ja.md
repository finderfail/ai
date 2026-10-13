# Git：コンフリクトの解決

コンフリクトが起きると、git はファイル内の該当箇所に印を付けます：

```
<<<<<<< HEAD
あなたの変更
=======
取り込む側の変更
>>>>>>> feature/login
```

手順：
1. `git status` でコンフリクトしたファイルを確認。
2. 各ファイルを開き、必要な内容を残して `<<<<<<<`、`=======`、`>>>>>>>` の印を消す。
3. `git add ファイル` で解決済みにする。
4. `git commit`（merge の場合）または `git rebase --continue`（rebase の場合）。

片方を丸ごと採用：`git checkout --ours ファイル` / `git checkout --theirs ファイル`。やめる場合は `git merge --abort` / `git rebase --abort`。
