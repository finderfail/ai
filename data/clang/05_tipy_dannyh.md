# Типы данных

```c
#include <stdio.h>
#include <stdint.h>

int main(void) {
    char c = 'A';
    int i = 42;
    long l = 1000000L;
    float f = 3.14f;
    double d = 3.141592653589793;
    unsigned int u = 4000000000u;

    int32_t exact = 100;
    uint64_t big = 18000000000ULL;

    printf("%c %d %ld %f %lf %u\n", c, i, l, f, d, u);
    printf("размер int: %zu байт\n", sizeof(int));
    return 0;
}
```

Размеры типов зависят от платформы, гарантируется только `sizeof(char) == 1`. Когда нужен точный размер, используют типы из `<stdint.h>`: `int8_t`, `int32_t`, `uint64_t`.
