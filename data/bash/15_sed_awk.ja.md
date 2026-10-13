# Bash：sed と awk によるテキスト編集

```bash
sed 's/old/new/' file          # 各行の最初の一致を置換
sed 's/old/new/g' file         # すべての一致を置換
sed -i 's/old/new/g' file      # ファイルを直接編集（GNU/Linux）
sed -i '' 's/old/new/g' file   # 同じ操作を macOS（BSD sed）で
sed -n '10,20p' file           # 10〜20行目を表示
sed '/^$/d' file               # 空行を削除

awk '{print $1}' file          # 1列目（空白区切り）
awk -F, '{print $2}' data.csv  # CSV の2列目
awk '$3 > 100' file            # 3列目が100より大きい行
awk '{s += $2} END {print s}' file   # 2列目の合計
```

macOS の `sed -i` は `-i` の後に引数（空文字列 `''`）が必要です。スクリプトを移植するときによくあるエラーの原因です。
