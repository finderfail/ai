# Bash：find と xargs によるファイル検索

```bash
find . -name "*.log"                 # 名前で検索
find . -iname "readme*"              # 大文字小文字を区別しない
find . -type d -name node_modules    # ディレクトリのみ
find . -type f -size +100M           # 100MB より大きいファイル
find . -mtime -1                     # 直近1日以内に変更
find . -name "*.tmp" -delete         # 見つけて削除
find . -name "*.py" -exec wc -l {} +     # コマンドを実行

find . -name "*.txt" -print0 | xargs -0 grep "hello"
```

`xargs` と組み合わせるときは `-print0` と `-0` を使います。空白を含む名前でも壊れません。`-delete` の前に、まず `-delete` なしで実行して一覧を確認してください。
