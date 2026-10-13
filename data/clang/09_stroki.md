# Строки

Строка в C — это массив `char`, завершённый нулевым байтом `'\0'`.

```c
#include <string.h>

char greeting[] = "Привет";
const char *literal = "только для чтения";
char buffer[64];

strcpy(buffer, "текст");
strncpy(buffer, "текст", sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';

size_t len = strlen(greeting);
int cmp = strcmp("abc", "abd");
strcat(buffer, " ещё");
char *found = strchr(buffer, 'к');
```

`strlen` не считает нулевой байт, поэтому под строку из N символов нужен массив на N+1. `strcpy` не проверяет размер приёмника — предпочитайте `strncpy` или `snprintf`. Строковые литералы нельзя изменять.
