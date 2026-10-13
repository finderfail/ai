# Препроцессор

```c
#include <stdio.h>

#define MAX_SIZE 100
#define SQUARE(x) ((x) * (x))
#define DEBUG 1

#if DEBUG
    #define LOG(msg) printf("[debug] %s\n", msg)
#else
    #define LOG(msg)
#endif

#ifndef HEADER_GUARD_H
#define HEADER_GUARD_H
/* содержимое заголовочного файла */
#endif
```

Аргументы макроса обязательно оборачивают в скобки: без них `SQUARE(1 + 2)` развернётся в `1 + 2 * 1 + 2` и даст 5 вместо 9. Защита заголовка через `#ifndef` предотвращает повторное включение.
