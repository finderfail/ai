# HTML/CSS の例: ダッシュボードのグリッド

Grid によるサイズの異なるウィジェット。

```html
<div class="dash">
  <div class="w big">Chart</div><div class="w">KPI</div><div class="w">KPI</div>
  <div class="w tall">Activity</div><div class="w wide">Table</div>
</div>
```

```css
.dash { display: grid; grid-template-columns: repeat(4, 1fr); grid-auto-rows: 140px; gap: 16px; padding: 16px; }
.w { border-radius: 14px; background: #fff; border: 1px solid #e5e7eb; padding: 16px; }
.big { grid-column: span 2; grid-row: span 2; }
.tall { grid-row: span 2; }
.wide { grid-column: span 3; }
@media (max-width: 900px) { .dash { grid-template-columns: 1fr 1fr; } .wide { grid-column: span 2; } }
```
