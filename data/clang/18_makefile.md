# Makefile

```makefile
CC = gcc
CFLAGS = -std=c17 -Wall -Wextra -g
TARGET = program
OBJS = main.o math_utils.o

$(TARGET): $(OBJS)
	$(CC) $(OBJS) -o $(TARGET)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS) $(TARGET)

.PHONY: clean
```

Отступы в Makefile обязаны быть символами табуляции, а не пробелами — иначе make выдаст ошибку. Запуск: `make` для сборки, `make clean` для очистки.
