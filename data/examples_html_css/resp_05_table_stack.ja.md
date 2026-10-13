# HTML/CSS の例: スマホでカード化する表

狭い画面で表の行がカードになる。

```html
<table class="rt"><thead><tr><th>Name</th><th>Plan</th></tr></thead>
<tbody><tr><td data-label="Name">Ann</td><td data-label="Plan">Pro</td></tr></tbody></table>
```

```css
@media (max-width: 600px) {
  .rt thead { display: none; }
  .rt tr { display: block; margin-bottom: 12px; padding: 8px; border: 1px solid #eee; border-radius: 10px; }
  .rt td { display: flex; justify-content: space-between; padding: 6px 4px; }
  .rt td::before { content: attr(data-label); font-weight: 600; color: #666; }
}
```
