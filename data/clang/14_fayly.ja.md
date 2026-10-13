# ファイル操作

```c
#include <stdio.h>

int main(void) {
    FILE *out = fopen("data.txt", "w");
    if (out == NULL) {
        perror("ファイルを開けませんでした");
        return 1;
    }
    fprintf(out, "行 %d\n", 1);
    fclose(out);

    FILE *in = fopen("data.txt", "r");
    if (in == NULL) {
        return 1;
    }

    char line[256];
    while (fgets(line, sizeof(line), in) != NULL) {
        printf("%s", line);
    }
    fclose(in);
    return 0;
}
```

モード：`"r"` 読み取り、`"w"` 書き込み（内容を空にする）、`"a"` 追記、`"rb"` と `"wb"` はバイナリ用。`fopen` の結果は必ず `NULL` か確認します。`fgets` は、規格から削除された `gets` より安全です。
