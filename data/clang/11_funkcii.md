# Функции

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

Аргументы передаются по значению — чтобы функция изменила переменную вызывающего кода, передают указатель. Прототип перед `main` позволяет вызывать функцию, определённую ниже.
