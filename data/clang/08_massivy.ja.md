# 配列

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

添字は0から始まります。配列の範囲外アクセスはチェックされず、未定義動作になります。C の脆弱性の主な原因の1つです。`sizeof(arr) / sizeof(arr[0])` は配列を宣言した場所でだけ使え、配列を渡された関数の中では使えません。
