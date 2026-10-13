# Bash：よくあるミス

- `=` の前後の空白：`x = 1` はエラー、`x=1` と書きます。
- 引用符のない変数：`rm $f` は空白を含む名前で壊れます。`rm "$f"` と書きます。
- `command not found`：プログラムが未インストールか `$PATH` にありません。確認：`command -v prog`。
- スクリプト実行時の `Permission denied`：`chmod +x` していない。書き込み時ならディレクトリの権限不足。
- `bad interpreter: /bin/bash^M`：改行コードが Windows（CRLF）。修正：`sed -i 's/\r$//' script.sh` または `dos2unix`。
- `[: missing ]`：条件式の `]` の前に空白がない。
- `~/.bashrc` の変更が反映されない：`source ~/.bashrc` を実行するか、新しいターミナルを開きます。
- スクリプト内の `cd` は呼び出し元のシェルには影響しません（別プロセスで動くため）。
