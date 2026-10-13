# Git：プルリクエスト（マージリクエスト）での作業

1. main を更新：`git switch main && git pull`。
2. ブランチを作成：`git switch -c feature/short-name`。
3. 小さな単位でコミットし、`git push -u origin feature/short-name`。
4. GitHub/GitLab でプルリクエストを作成し、何をなぜ変えたかを書く。
5. レビューの指摘は同じブランチへの新しいコミットで直して push する。
6. main が先に進んだら、自分のブランチで `git pull --rebase origin main` か `git merge main`。
7. マージ後、ブランチをローカルとサーバーの両方で削除する。

GitHub CLI なら：`gh pr create`、`gh pr status`、`gh pr checkout 123`。
