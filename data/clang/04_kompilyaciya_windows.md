# Компиляция на Windows

Есть три распространённых пути.

**MSVC (Visual Studio)** — установите Visual Studio с компонентом «Разработка классических приложений на C++», затем в «Developer Command Prompt»:

```cmd
cl program.c
program.exe
```

**MinGW-w64** — порт GCC под Windows, ставится через MSYS2:

```bash
pacman -S mingw-w64-ucrt-x86_64-gcc
gcc program.c -o program.exe
```

**WSL** — подсистема Linux внутри Windows, дальше всё как в Linux:

```bash
wsl --install
gcc program.c -o program
```

В MSVC исполняемый файл получает расширение `.exe` автоматически. При использовании GCC его нужно указывать явно в `-o`.

Ключевые слова: винда, виндовс, Windows, MSVC, MinGW, WSL, собрать, скомпилировать программу на си под винду.
