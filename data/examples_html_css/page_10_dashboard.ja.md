# HTML/CSS の例: 管理画面の骨組み

サイドバー、トップバー、ウィジェットのグリッド。

```html
<div class="dash"><aside>Menu</aside><header>Top bar</header>
<main><div class="widget">Users</div><div class="widget">Revenue</div><div class="widget wide">Chart</div></main></div>
```

```css
.dash { display: grid; grid-template: "side top" 56px "side main" 1fr / 220px 1fr; min-height: 100dvh; }
.dash aside { grid-area: side; background: #111827; color: #fff; padding: 16px; }
.dash header { grid-area: top; display: flex; align-items: center; padding: 0 20px; border-bottom: 1px solid #e5e7eb; }
.dash main { grid-area: main; display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; padding: 20px; align-content: start; }
.widget { padding: 20px; border-radius: 14px; background: #f9fafb; }
.wide { grid-column: 1 / -1; min-height: 240px; }
```
