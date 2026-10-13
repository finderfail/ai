# Git：ファイルの変更を取り消す

```bash
git restore file.py            # 作業フォルダの変更を取り消す（元に戻せない）
git restore --staged file.py   # インデックスから外す（変更は残る）
git restore --source=HEAD~2 file.py   # 2つ前のコミットの状態に戻す
git clean -n                   # 削除対象の未追跡ファイルを表示
git clean -fd                  # 未追跡のファイルとフォルダを削除
```

古い書き方：`git restore file.py` の代わりに `git checkout -- file.py`、`git restore --staged file.py` の代わりに `git reset HEAD file.py`。

`git restore` と `git clean -f` は保存していない作業を復元不能な形で消します。先に `git status` と `git clean -n` で確認してください。
