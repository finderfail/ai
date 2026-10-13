# Компиляция на macOS

На macOS компилятором служит Clang, он входит в Command Line Tools:

```bash
xcode-select --install
```

Проверка и сборка:

```bash
clang --version
clang program.c -o program
./program
```

Команда `gcc` на macOS обычно является псевдонимом для Clang — обе работают одинаково. Флаги те же, что и у GCC: `-Wall -Wextra -g -O2 -std=c17`.

Для установки настоящего GCC используют Homebrew: `brew install gcc`, после чего он доступен как `gcc-14`.

Ключевые слова: мак, макось, macOS, макбук, MacBook, Apple, clang, xcode, собрать, скомпилировать программу на си под мак.
