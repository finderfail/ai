# Bash: циклы for, while, until

```bash
for f in *.log; do
  gzip "$f"
done

for i in {1..5}; do echo "$i"; done

for ((i = 0; i < 3; i++)); do echo "$i"; done

while read -r line; do
  echo "строка: $line"
done < input.txt

n=0
until (( n >= 3 )); do n=$((n + 1)); done
```

Для чтения файла построчно используйте `while read -r line`, а не `for line in $(cat file)` — последний разбивает по пробелам, а не по строкам. `break` выходит из цикла, `continue` переходит к следующей итерации.
