# Git：履歴と差分

```bash
git log --oneline              # 簡潔な履歴
git log --oneline --graph --all    # 全ブランチのグラフ
git log -p file.py             # ファイルの変更履歴
git log --author="Ilya" --since="2 weeks ago"
git show HEAD                  # 最新コミットとその変更
git show abc1234:path/file.py  # 指定コミット時点のファイル

git diff                       # まだインデックスにない変更
git diff --staged              # 次のコミットに入る変更
git diff main..feature         # ブランチ間の差分
git blame file.py              # 各行を誰がいつ変更したか
```
