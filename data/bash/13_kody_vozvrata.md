# Bash: коды возврата и обработка ошибок

Каждая команда возвращает код: `0` — успех, любое другое число — ошибка. Код последней команды — в `$?`.

```bash
grep -q "error" log.txt
echo $?                      # 0 — нашёл, 1 — не нашёл

mkdir build && cd build      # cd только если mkdir успешен
cd /nope || exit 1           # выйти, если cd не удался

if ! command -v git >/dev/null; then
  echo "git не установлен" >&2
  exit 1
fi

trap 'echo "ошибка в строке $LINENO" >&2' ERR
trap 'rm -f "$tmp"' EXIT     # уборка при любом выходе
```

Сообщения об ошибках выводите в stderr: `echo "..." >&2`.
