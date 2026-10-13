# HTML/CSS の例: ステータス付きの表

caption と色付きのステータス。

```html
<table class="orders"><caption>Recent orders</caption>
<tr><td>#1042</td><td><span class="status paid">Paid</span></td></tr>
<tr><td>#1043</td><td><span class="status pending">Pending</span></td></tr></table>
```

```css
.orders caption { text-align: left; font-weight: 700; padding-bottom: 8px; }
.status { padding: 2px 10px; border-radius: 999px; font-size: 12px; font-weight: 600; }
.paid { background: #dcfce7; color: #166534; }
.pending { background: #fef3c7; color: #92400e; }
```
