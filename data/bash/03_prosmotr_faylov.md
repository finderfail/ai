# Bash: просмотр содержимого файлов

```bash
cat file.txt         # вывести весь файл
less file.txt        # постраничный просмотр (q — выход, / — поиск)
head -n 20 file.txt  # первые 20 строк
tail -n 20 file.txt  # последние 20 строк
tail -f app.log      # следить за файлом в реальном времени
wc -l file.txt       # число строк
wc -w file.txt       # число слов
du -sh dir/          # размер каталога
df -h                # свободное место на дисках
file image.png       # определить тип файла
```
