# Windows でのコンパイル

よく使われる方法は3つあります。

**MSVC（Visual Studio）**：「C++ によるデスクトップ開発」コンポーネント付きで Visual Studio を入れ、「Developer Command Prompt」で：

```cmd
cl program.c
program.exe
```

**MinGW-w64**：Windows 向けの GCC。MSYS2 で入れます：

```bash
pacman -S mingw-w64-ucrt-x86_64-gcc
gcc program.c -o program.exe
```

**WSL**：Windows 内の Linux サブシステム。あとは Linux と同じです：

```bash
wsl --install
gcc program.c -o program
```

MSVC では実行ファイルに `.exe` が自動で付きます。GCC では `-o` で明示する必要があります。

キーワード：Windows、MSVC、MinGW、WSL、ビルド、Windows で C をコンパイル。
