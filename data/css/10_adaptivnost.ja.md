# CSS：レスポンシブとメディアクエリ

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

**モバイルファースト**：スマートフォン向けを基本にし、大きな画面向けに拡張する。
```css
.grid { display: grid; gap: 16px; grid-template-columns: 1fr; }
@media (min-width: 768px)  { .grid { grid-template-columns: repeat(2, 1fr); } }
@media (min-width: 1200px) { .grid { grid-template-columns: repeat(3, 1fr); } }

@media (prefers-color-scheme: dark) { body { background: #161618; color: #f1f1f4; } }
@media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }
@media (hover: none) { .tooltip { display: none; } }
```

**コンテナクエリ**：ウィンドウではなく親のサイズで切り替える：
```css
.card-wrap { container-type: inline-size; }
@container (min-width: 400px) { .card { display: flex; } }
```

画像：`img { max-width: 100%; height: auto; }`。
