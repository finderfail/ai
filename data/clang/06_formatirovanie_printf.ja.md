# printf と scanf の書式指定子

| 指定子 | 型 |
|---|---|
| `%d` | int |
| `%u` | unsigned int |
| `%ld` | long |
| `%lld` | long long |
| `%f` | float、printf での double |
| `%lf` | scanf での double |
| `%c` | char |
| `%s` | 文字列 |
| `%p` | ポインタ |
| `%zu` | size_t |
| `%x` | 16進数 |
| `%%` | % 記号そのもの |

```c
printf("%5d|\n", 42);      /* 幅5:      42| */
printf("%-5d|\n", 42);     /* 左寄せ: 42   | */
printf("%.2f\n", 3.14159); /* 小数2桁: 3.14 */
```

指定子と引数の型が合わないと、コンパイルエラーではなく未定義動作になります。
