# HTML/CSS の例: 高さがそろう列

下にボタンがある同じ高さの3列。

```html
<div class="cols"><div class="col"><p>Text</p><a href="#">More</a></div><div class="col"><p>Longer text here</p><a href="#">More</a></div></div>
```

```css
.cols { display: grid; grid-auto-flow: column; grid-auto-columns: 1fr; gap: 16px; }
.col { display: flex; flex-direction: column; padding: 16px; border: 1px solid #ddd; border-radius: 12px; }
.col p { flex: 1; }
@media (max-width: 700px) { .cols { grid-auto-flow: row; } }
```
