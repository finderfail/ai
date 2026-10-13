# Bash: массивы и операции со строками

```bash
arr=(one two three)
echo "${arr[0]}"        # первый элемент
echo "${arr[@]}"        # все элементы
echo "${#arr[@]}"       # длина массива
arr+=(four)             # добавить
for x in "${arr[@]}"; do echo "$x"; done

s="hello world"
echo "${#s}"            # длина строки
echo "${s:0:5}"         # подстрока: hello
echo "${s/world/bash}"  # замена первого вхождения
file="photo.jpg"
echo "${file%.jpg}"     # убрать суффикс: photo
echo "${file##*.}"      # расширение: jpg
```

`"${arr[@]}"` в кавычках сохраняет элементы с пробелами как отдельные.
