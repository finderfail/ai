# コマンドライン引数

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "使い方: %s <数値>\n", argv[0]);
        return 1;
    }

    long value = strtol(argv[1], NULL, 10);
    printf("受け取った値: %ld\n", value);

    for (int i = 0; i < argc; i++) {
        printf("argv[%d] = %s\n", i, argv[i]);
    }
    return 0;
}
```

`argv[0]` はプログラム自身の名前なので、ユーザーの引数は `argv[1]` から始まり、`argc` は常に1以上です。`strtol` は解析エラーを検出できるので `atoi` より望ましいです。
