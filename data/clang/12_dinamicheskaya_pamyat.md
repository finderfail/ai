# Динамическая память

```c
#include <stdlib.h>

int *array = malloc(10 * sizeof(int));
if (array == NULL) {
    return 1;
}

for (int i = 0; i < 10; i++) {
    array[i] = i;
}

int *bigger = realloc(array, 20 * sizeof(int));
if (bigger == NULL) {
    free(array);
    return 1;
}
array = bigger;

int *zeroed = calloc(10, sizeof(int));

free(array);
free(zeroed);
array = NULL;
```

Каждому `malloc` должен соответствовать ровно один `free`. `malloc` не обнуляет память, `calloc` обнуляет. Результат `realloc` нужно присваивать во временную переменную — иначе при неудаче потеряется исходный указатель. После `free` указателю присваивают `NULL`, чтобы не использовать освобождённую память.
