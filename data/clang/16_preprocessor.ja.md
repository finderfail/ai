# プリプロセッサ

```c
#include <stdio.h>

#define MAX_SIZE 100
#define SQUARE(x) ((x) * (x))
#define DEBUG 1

#if DEBUG
    #define LOG(msg) printf("[debug] %s\n", msg)
#else
    #define LOG(msg)
#endif

#ifndef HEADER_GUARD_H
#define HEADER_GUARD_H
/* ヘッダーファイルの内容 */
#endif
```

マクロの引数は必ずかっこで囲みます。かっこがないと `SQUARE(1 + 2)` は `1 + 2 * 1 + 2` に展開され、9 ではなく 5 になります。`#ifndef` によるインクルードガードで二重読み込みを防ぎます。
