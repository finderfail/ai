# 構造体

```c
#include <string.h>

struct Point {
    int x;
    int y;
};

typedef struct {
    char name[64];
    int age;
    double salary;
} Employee;

int main(void) {
    struct Point p = {10, 20};
    Employee e = {"Taro", 30, 1500.0};

    p.x = 15;
    strcpy(e.name, "Jiro");

    Employee *ptr = &e;
    ptr->age = 31;

    return 0;
}
```

変数からはドット、ポインタからは矢印 `->` でフィールドにアクセスします。`typedef` を使うと、宣言のたびに `struct` と書かずに済みます。
