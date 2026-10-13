# デバッグ

デバッグ情報付きでビルドし、デバッガを起動します：

```bash
gcc -g -Wall program.c -o program
gdb ./program
```

GDB の主なコマンド：`break main` でブレークポイント、`run` で実行、`next` で1行実行、`step` で関数の中へ、`print x` で値を表示、`backtrace` で呼び出しスタック、`continue` で続行。

macOS では GDB の代わりに LLDB がよく使われます：`lldb ./program`。コマンドは似ています（`b main`、`r`、`n`、`p x`、`bt`）。

メモリ関連のバグを探す：

```bash
gcc -fsanitize=address -g program.c -o program
./program

valgrind --leak-check=full ./program
```

AddressSanitizer は、範囲外アクセスや解放済みメモリへのアクセスを実行中に検出します。
