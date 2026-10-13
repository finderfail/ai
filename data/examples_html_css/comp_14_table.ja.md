# HTML/CSS の例: ストライプの表

ゼブラ模様と hover の見やすい表。

```html
<table class="table">
  <thead><tr><th>Name</th><th>Plan</th><th>Status</th></tr></thead>
  <tbody><tr><td>Ann</td><td>Pro</td><td>Active</td></tr><tr><td>Kei</td><td>Free</td><td>Trial</td></tr></tbody>
</table>
```

```css
.table { width: 100%; border-collapse: collapse; font-size: 14px; }
.table th, .table td { padding: 12px; text-align: left; border-bottom: 1px solid #eee; }
.table thead th { background: #f8fafc; font-weight: 600; }
.table tbody tr:nth-child(even) { background: #fafafa; }
.table tbody tr:hover { background: #eef2ff; }
```
