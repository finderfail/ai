# Многофайловые проекты

`math_utils.h`:

```c
#ifndef MATH_UTILS_H
#define MATH_UTILS_H

int add(int a, int b);

#endif
```

`math_utils.c`:

```c
#include "math_utils.h"

int add(int a, int b) {
    return a + b;
}
```

`main.c`:

```c
#include <stdio.h>
#include "math_utils.h"

int main(void) {
    printf("%d\n", add(2, 3));
    return 0;
}
```

Сборка:

```bash
gcc -c math_utils.c -o math_utils.o
gcc -c main.c -o main.o
gcc math_utils.o main.o -o program
```

Или одной командой: `gcc main.c math_utils.c -o program`. Свои заголовки подключают кавычками, системные — угловыми скобками.
