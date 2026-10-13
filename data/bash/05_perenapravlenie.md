# Bash: перенаправление ввода и вывода

```bash
cmd > out.txt        # stdout в файл (перезаписать)
cmd >> out.txt       # stdout в файл (дописать)
cmd 2> err.txt       # stderr в файл
cmd > all.txt 2>&1   # stdout и stderr в один файл
cmd &> all.txt       # то же самое, короче (bash)
cmd 2>/dev/null      # выбросить ошибки
cmd < input.txt      # подать файл на stdin
```

Порядок важен: `cmd > f 2>&1` пишет обе ветки в файл, а `cmd 2>&1 > f` — нет (stderr уйдёт на экран).

`tee` одновременно пишет в файл и на экран: `make 2>&1 | tee build.log`.
