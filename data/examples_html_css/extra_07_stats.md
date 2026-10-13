# Пример HTML/CSS: блок статистики

Крупные цифры KPI в ряд.

```html
<section class="stats"><div><b>12k</b><span>Users</span></div><div><b>99.9%</b><span>Uptime</span></div><div><b>24/7</b><span>Support</span></div></section>
```

```css
.stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 16px; text-align: center; }
.stats b { display: block; font-size: clamp(28px, 5vw, 44px); font-variant-numeric: tabular-nums; }
.stats span { color: #6b7280; }
```
