# Git：直前のコミットを修正する

```bash
git commit --amend -m "新しいメッセージ"   # メッセージを修正
git add forgotten.py
git commit --amend --no-edit              # 忘れたファイルを同じコミットに追加
git commit --amend --author="名前 <mail@example.com>" --no-edit
```

`--amend` は直前のコミットを新しいコミット（別のハッシュ）に置き換えます。すでに push 済みなら、amend の後に `git push --force-with-lease` が必要になるため、共有ブランチでは避けましょう。

もっと前のコミットを直すには `git rebase -i HEAD~N` で `edit` か `reword` を指定します。
