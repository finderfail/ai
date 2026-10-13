# Аргументы командной строки

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Использование: %s <число>\n", argv[0]);
        return 1;
    }

    long value = strtol(argv[1], NULL, 10);
    printf("получено: %ld\n", value);

    for (int i = 0; i < argc; i++) {
        printf("argv[%d] = %s\n", i, argv[i]);
    }
    return 0;
}
```

`argv[0]` — имя самой программы, поэтому пользовательские аргументы начинаются с `argv[1]`, а `argc` всегда не меньше единицы. `strtol` предпочтительнее `atoi`, потому что позволяет обнаружить ошибку разбора.
