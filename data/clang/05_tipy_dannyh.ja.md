# データ型

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
    printf("int のサイズ: %zu バイト\n", sizeof(int));
    return 0;
}
```

型のサイズはプラットフォームに依存し、保証されているのは `sizeof(char) == 1` だけです。正確なサイズが必要なときは `<stdint.h>` の型を使います：`int8_t`、`int32_t`、`uint64_t`。
