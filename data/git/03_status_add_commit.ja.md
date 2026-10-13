# Git：基本サイクル — status・add・commit

```bash
git status                 # 変更内容とインデックスの状態
git add file.py            # ファイルをインデックスに追加（ステージ）
git add .                  # 現在のフォルダの変更をすべて追加
git add -p                 # 変更を部分ごとに選んで追加
git commit -m "メールアドレスの検証を追加"
git commit -am "..."       # 追跡中のファイルを add してコミット
```

3つの状態：作業フォルダ → インデックス（`git add`）→ コミット（`git commit`）。新しいファイルは `commit -a` では含まれないので、先に `git add` が必要です。

論理的にまとまった小さな単位でコミットしましょう。
