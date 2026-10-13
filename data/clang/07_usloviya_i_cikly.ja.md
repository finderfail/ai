# 条件分岐とループ

```c
int x = 10;

if (x > 5) {
    puts("5より大きい");
} else if (x == 5) {
    puts("ちょうど5");
} else {
    puts("5より小さい");
}

switch (x) {
    case 1:
        puts("1");
        break;
    case 10:
        puts("10");
        break;
    default:
        puts("その他");
}

for (int i = 0; i < 5; i++) {
    printf("%d ", i);
}

int n = 3;
while (n > 0) {
    n--;
}

do {
    n++;
} while (n < 3);
```

`switch` で `break` を忘れると次の case に「フォールスルー」します。よくあるミスです。C には `<stdbool.h>` 以前は bool 型がなく、0 が偽、0 以外がすべて真です。
