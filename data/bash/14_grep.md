# Bash: поиск текста с grep

```bash
grep "error" app.log            # строки, содержащие error
grep -i "error" app.log         # без учёта регистра
grep -n "TODO" *.py             # с номерами строк
grep -r "API_KEY" .             # рекурсивно по каталогу
grep -rl "import os" src/       # только имена файлов
grep -v "^#" config.conf        # строки, НЕ начинающиеся с #
grep -c "500" access.log        # число совпадений
grep -E "warn|error" app.log    # расширенные регулярки: или
grep -w "id" file               # только целое слово
grep -A 3 -B 1 "Traceback" log  # контекст: 3 после, 1 до
```

Если установлен `rg` (ripgrep) — он быстрее и сам пропускает файлы из .gitignore.
