# 動的メモリ

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

`malloc` 1回につき `free` はちょうど1回。`malloc` はメモリをゼロにせず、`calloc` はゼロにします。`realloc` の結果は一時変数で受けます。失敗したときに元のポインタを失わないためです。`free` の後はポインタに `NULL` を代入し、解放済みメモリを使わないようにします。
