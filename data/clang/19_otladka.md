# Отладка

Сборка с отладочной информацией и запуск отладчика:

```bash
gcc -g -Wall program.c -o program
gdb ./program
```

Основные команды GDB: `break main` ставит точку останова, `run` запускает, `next` выполняет строку, `step` заходит внутрь функции, `print x` печатает значение, `backtrace` показывает стек вызовов, `continue` продолжает выполнение.

На macOS вместо GDB обычно используют LLDB: `lldb ./program`, команды похожи (`b main`, `r`, `n`, `p x`, `bt`).

Поиск ошибок работы с памятью:

```bash
gcc -fsanitize=address -g program.c -o program
./program

valgrind --leak-check=full ./program
```

AddressSanitizer ловит выход за границы и обращение к освобождённой памяти прямо во время выполнения.
