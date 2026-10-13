# CSS：読み込み、カスケード、詳細度

読み込み方：
```html
<link rel="stylesheet" href="styles.css">
<style> p { color: #333; } </style>
<p style="color: red">インラインスタイル</p>
```

**カスケード** は、複数のルールがあるときにどれを適用するかを決める：
1. 重要度：`!important` は通常のルールより強い。
2. 出所とレイヤー（`@layer`）：作者のスタイルはブラウザのスタイルより強い。
3. セレクターの **詳細度**。
4. 順序：同じなら後に書いたルールが勝つ。

**詳細度** は（ID、クラス、タグ）の組で数える：
- `#menu` → (1,0,0)、`.btn`・`[type="text"]`・`:hover` → (0,1,0)、`p`・`::before` → (0,0,1)。
- `#nav .item a` → (1,1,1) は `.nav .item a` → (0,2,1) より強い。
- インラインの `style="..."` はどのセレクターよりも強い。

**継承**：フォント、色、`line-height` は子孫に継承されるが、`margin`、`padding`、`border`、`background` は継承されない。`inherit`、`initial`、`unset`、`revert` で明示的に制御できる。

スタイルでの `!important` や ID の多用は、上書きを難しくするので避ける。
