# Структуры

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
    Employee e = {"Иван", 30, 1500.0};

    p.x = 15;
    strcpy(e.name, "Пётр");

    Employee *ptr = &e;
    ptr->age = 31;

    return 0;
}
```

К полям через переменную обращаются точкой, через указатель — стрелкой `->`. `typedef` избавляет от необходимости писать `struct` при каждом объявлении.
