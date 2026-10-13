# Работа с файлами

```c
#include <stdio.h>

int main(void) {
    FILE *out = fopen("data.txt", "w");
    if (out == NULL) {
        perror("не удалось открыть файл");
        return 1;
    }
    fprintf(out, "строка %d\n", 1);
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

Режимы: `"r"` чтение, `"w"` запись с обнулением файла, `"a"` дозапись, `"rb"` и `"wb"` для двоичных данных. Результат `fopen` всегда проверяют на `NULL`. `fgets` безопаснее `gets`, которая удалена из стандарта.
