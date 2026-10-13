# Пример HTML/CSS: аккуратная таблица данных

Шапка, разделители, выравнивание чисел вправо.

```html
<table class="data"><thead><tr><th>Product</th><th class="num">Price</th></tr></thead>
<tbody><tr><td>Plan Pro</td><td class="num">$12</td></tr></tbody></table>
```

```css
.data { width: 100%; border-collapse: collapse; font-size: 14px; }
.data th, .data td { padding: 10px 12px; border-bottom: 1px solid #e5e7eb; text-align: left; }
.data th { font-weight: 600; color: #374151; background: #f9fafb; }
.data .num { text-align: right; font-variant-numeric: tabular-nums; }
```
