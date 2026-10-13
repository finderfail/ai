# ポインタ

```c
int value = 42;
int *ptr = &value;

printf("%d\n", *ptr);
printf("%p\n", (void *)ptr);

*ptr = 100;

int *null_ptr = NULL;
if (null_ptr != NULL) {
    printf("%d\n", *null_ptr);
}
```

`&` は変数のアドレスを取り、`*` はポインタを参照外しします。`NULL` や未初期化のポインタを参照外しするとプログラムがクラッシュします。

ポインタと配列は密接に関係しています。式の中の配列名は先頭要素へのポインタに変換されます。

```c
int arr[3] = {10, 20, 30};
int *p = arr;
printf("%d %d\n", p[1], *(p + 2));
```
