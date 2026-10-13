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

Makefile のインデントは空白ではなく必ずタブ文字にします。そうでないと make がエラーを出します。実行：ビルドは `make`、後片付けは `make clean`。
