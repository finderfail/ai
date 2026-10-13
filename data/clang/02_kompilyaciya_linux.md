# Компиляция на Linux

Компилятор GCC обычно уже установлен. Если нет:

```bash
sudo apt install build-essential      # Debian, Ubuntu
sudo dnf install gcc make             # Fedora
sudo pacman -S base-devel             # Arch
```

Сборка и запуск:

```bash
gcc program.c -o program
./program
```

Полезные флаги: `-Wall -Wextra` включают предупреждения, `-g` добавляет отладочную информацию, `-O2` включает оптимизацию, `-std=c17` задаёт стандарт языка.

```bash
gcc -std=c17 -Wall -Wextra -g program.c -o program
```

Ключевые слова: линукс, Linux, Ubuntu, Debian, Fedora, Arch, gcc, собрать, скомпилировать программу на си.
