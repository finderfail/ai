# HTML/CSS の例: モバイルファーストのグリッド

スマホで1列、大きな画面で2列と4列。

```html
<div class="products">…</div>
```

```css
.products { display: grid; gap: 16px; grid-template-columns: 1fr; }
@media (min-width: 640px) { .products { grid-template-columns: repeat(2, 1fr); } }
@media (min-width: 1024px) { .products { grid-template-columns: repeat(4, 1fr); } }
```
