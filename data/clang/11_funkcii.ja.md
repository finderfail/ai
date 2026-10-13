# 関数

```c
#include <stdio.h>

int add(int a, int b);

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int add(int a, int b) {
    return a + b;
}

int main(void) {
    int x = 1, y = 2;
    swap(&x, &y);
    printf("%d %d %d\n", x, y, add(x, y));
    return 0;
}
```

引数は値渡しです。呼び出し側の変数を関数内で変更したい場合はポインタを渡します。`main` の前にプロトタイプを書くと、後ろで定義した関数を呼び出せます。
