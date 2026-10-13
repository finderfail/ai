# Bash：for・while・until ループ

```bash
for f in *.log; do
  gzip "$f"
done

for i in {1..5}; do echo "$i"; done

for ((i = 0; i < 3; i++)); do echo "$i"; done

while read -r line; do
  echo "行: $line"
done < input.txt

n=0
until (( n >= 3 )); do n=$((n + 1)); done
```

ファイルを1行ずつ読むには `while read -r line` を使います。`for line in $(cat file)` は行ではなく空白で区切ってしまいます。`break` でループを抜け、`continue` で次の繰り返しへ進みます。
