# 文字列

C の文字列は、ヌル文字 `'\0'` で終わる `char` の配列です。

```c
#include <string.h>

char greeting[] = "こんにちは";
const char *literal = "読み取り専用";
char buffer[64];

strcpy(buffer, "テキスト");
strncpy(buffer, "テキスト", sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';

size_t len = strlen(greeting);
int cmp = strcmp("abc", "abd");
strcat(buffer, " 追加");
char *found = strchr(buffer, 'x');
```

`strlen` はヌル文字を数えないため、N 文字の文字列には N+1 の配列が必要です。`strcpy` はコピー先のサイズを確認しないので、`strncpy` か `snprintf` を使いましょう。文字列リテラルは変更できません。
