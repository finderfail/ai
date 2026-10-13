# Bash：grep によるテキスト検索

```bash
grep "error" app.log            # error を含む行
grep -i "error" app.log         # 大文字小文字を区別しない
grep -n "TODO" *.py             # 行番号付き
grep -r "API_KEY" .             # ディレクトリを再帰検索
grep -rl "import os" src/       # ファイル名だけ表示
grep -v "^#" config.conf        # # で始まらない行
grep -c "500" access.log        # 一致数
grep -E "warn|error" app.log    # 拡張正規表現：または
grep -w "id" file               # 単語単位で一致
grep -A 3 -B 1 "Traceback" log  # 前後の文脈：後3行、前1行
```

`rg`（ripgrep）が入っていれば、より高速で .gitignore のファイルも自動で除外します。
