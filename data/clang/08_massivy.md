# Массивы

```c
int numbers[5] = {1, 2, 3, 4, 5};
int zeros[10] = {0};
int auto_size[] = {1, 2, 3};

size_t count = sizeof(auto_size) / sizeof(auto_size[0]);

for (size_t i = 0; i < count; i++) {
    printf("%d ", auto_size[i]);
}

int matrix[2][3] = {
    {1, 2, 3},
    {4, 5, 6}
};
printf("%d\n", matrix[1][2]);
```

Индексация начинается с нуля. Выход за границы массива не проверяется — это неопределённое поведение и одна из главных причин уязвимостей в C. Приём `sizeof(arr) / sizeof(arr[0])` работает только там, где массив объявлен, но не внутри функции, куда он передан.
