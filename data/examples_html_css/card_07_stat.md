# Пример HTML/CSS: карточка-метрика

Показатель с подписью и изменением за период.

```html
<div class="stat">
  <p class="label">Revenue</p>
  <p class="value">$48,250</p>
  <p class="delta up">+12.4% vs last month</p>
</div>
```

```css
.stat { padding: 20px; border-radius: 16px; background: #fff; border: 1px solid #ececf1; min-width: 200px; }
.label { margin: 0; color: #777; font-size: 14px; }
.value { margin: 6px 0; font-size: 32px; font-weight: 800; font-variant-numeric: tabular-nums; }
.delta { margin: 0; font-size: 14px; }
.delta.up { color: #16a34a; } .delta.down { color: #dc2626; }
```
