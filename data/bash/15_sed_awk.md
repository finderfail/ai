# Bash: правка текста sed и awk

```bash
sed 's/old/new/' file          # заменить первое вхождение в строке
sed 's/old/new/g' file         # все вхождения
sed -i 's/old/new/g' file      # править файл на месте (GNU/Linux)
sed -i '' 's/old/new/g' file   # то же на macOS (BSD sed)
sed -n '10,20p' file           # вывести строки 10–20
sed '/^$/d' file               # удалить пустые строки

awk '{print $1}' file          # первый столбец (разделитель — пробелы)
awk -F, '{print $2}' data.csv  # второй столбец CSV
awk '$3 > 100' file            # строки, где 3-й столбец > 100
awk '{s += $2} END {print s}' file   # сумма 2-го столбца
```

`sed -i` на macOS требует аргумент после `-i` (пустую строку `''`) — частая причина ошибки при переносе скриптов.
