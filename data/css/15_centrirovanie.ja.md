# CSS：要素の中央寄せ

幅が決まったブロックを水平方向に：
```css
.box { width: 600px; margin-inline: auto; }
```

テキストとインライン要素：
```css
.text { text-align: center; }
```

Flexbox で両方向：
```css
.parent { display: flex; justify-content: center; align-items: center; min-height: 100vh; }
```

Grid（最も短い）：
```css
.parent { display: grid; place-items: center; min-height: 100vh; }
```

絶対位置指定：
```css
.parent { position: relative; }
.child  { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); }
```

画面中央のモーダル：
```css
.modal { position: fixed; inset: 0; margin: auto; width: min(90vw, 500px); height: fit-content; }
```

垂直方向に中央寄せするには、親に高さ（`min-height`）が必要。
