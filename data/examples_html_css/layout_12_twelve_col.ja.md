# HTML/CSS の例: 12カラムグリッド

Grid による伝統的な12カラムグリッド。

```html
<div class="row"><div class="col-8">Main</div><div class="col-4">Side</div></div>
```

```css
.row { display: grid; grid-template-columns: repeat(12, 1fr); gap: 24px; }
.col-4 { grid-column: span 4; } .col-6 { grid-column: span 6; }
.col-8 { grid-column: span 8; } .col-12 { grid-column: span 12; }
@media (max-width: 768px) { .row > * { grid-column: span 12; } }
```
