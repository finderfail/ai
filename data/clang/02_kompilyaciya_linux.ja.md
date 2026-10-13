# Linux でのコンパイル

GCC コンパイラはたいてい最初から入っています。ない場合：

```bash
sudo apt install build-essential      # Debian、Ubuntu
sudo dnf install gcc make             # Fedora
sudo pacman -S base-devel             # Arch
```

ビルドと実行：

```bash
gcc program.c -o program
./program
```

便利なフラグ：`-Wall -Wextra` で警告を有効化、`-g` でデバッグ情報を追加、`-O2` で最適化、`-std=c17` で言語規格を指定。

```bash
gcc -std=c17 -Wall -Wextra -g program.c -o program
```

キーワード：Linux、Ubuntu、Debian、Fedora、Arch、gcc、ビルド、C プログラムのコンパイル。
