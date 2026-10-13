# HTML/CSS の例: バッジ

色付きのステータスラベル。

```html
<span class="badge">New</span> <span class="badge green">Paid</span> <span class="badge red">Overdue</span>
```

```css
.badge { display: inline-block; padding: 2px 10px; border-radius: 999px; font-size: 12px; font-weight: 600;
  background: #eef2ff; color: #4338ca; }
.badge.green { background: #dcfce7; color: #166534; }
.badge.red { background: #fee2e2; color: #991b1b; }
```
