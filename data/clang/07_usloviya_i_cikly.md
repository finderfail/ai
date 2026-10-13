# Условия и циклы

```c
int x = 10;

if (x > 5) {
    puts("больше пяти");
} else if (x == 5) {
    puts("ровно пять");
} else {
    puts("меньше пяти");
}

switch (x) {
    case 1:
        puts("один");
        break;
    case 10:
        puts("десять");
        break;
    default:
        puts("другое");
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

Забытый `break` в `switch` приводит к «проваливанию» в следующий case — это частая ошибка. В C нет отдельного типа bool до `<stdbool.h>`: ноль это ложь, любое ненулевое значение — истина.
