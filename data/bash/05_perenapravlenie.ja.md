# Bash：入出力のリダイレクト

```bash
cmd > out.txt        # 標準出力をファイルへ（上書き）
cmd >> out.txt       # 標準出力をファイルへ（追記）
cmd 2> err.txt       # 標準エラーをファイルへ
cmd > all.txt 2>&1   # 標準出力と標準エラーを1つのファイルへ
cmd &> all.txt       # 同じ意味の短縮形（bash）
cmd 2>/dev/null      # エラーを捨てる
cmd < input.txt      # ファイルを標準入力に渡す
```

順序が重要です：`cmd > f 2>&1` は両方をファイルに書きますが、`cmd 2>&1 > f` では標準エラーは画面に出ます。

`tee` はファイルと画面の両方に出力します：`make 2>&1 | tee build.log`。
