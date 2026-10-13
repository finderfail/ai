# macOS でのコンパイル

macOS のコンパイラは Clang で、Command Line Tools に含まれています：

```bash
xcode-select --install
```

確認とビルド：

```bash
clang --version
clang program.c -o program
./program
```

macOS の `gcc` コマンドはたいてい Clang の別名で、どちらも同じように動きます。フラグは GCC と同じです：`-Wall -Wextra -g -O2 -std=c17`。

本物の GCC は Homebrew で入れます：`brew install gcc`。その後 `gcc-14` として使えます。

キーワード：Mac、macOS、MacBook、Apple、clang、xcode、ビルド、Mac で C をコンパイル。
