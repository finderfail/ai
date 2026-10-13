# Bash: поиск файлов find и xargs

```bash
find . -name "*.log"                 # по имени
find . -iname "readme*"              # без учёта регистра
find . -type d -name node_modules    # только каталоги
find . -type f -size +100M           # файлы больше 100 МБ
find . -mtime -1                     # изменённые за последние сутки
find . -name "*.tmp" -delete         # найти и удалить
find . -name "*.py" -exec wc -l {} +     # выполнить команду

find . -name "*.txt" -print0 | xargs -0 grep "hello"
```

С `xargs` используйте пару `-print0` / `-0`: так имена с пробелами не ломаются. Перед `-delete` сначала запустите ту же команду без `-delete` и проверьте список.
