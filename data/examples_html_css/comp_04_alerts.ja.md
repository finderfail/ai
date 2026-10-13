# HTML/CSS の例: アラート

成功、警告、エラーのメッセージ。

```html
<div class="alert success" role="status">Saved successfully.</div>
<div class="alert warning">Your trial ends in 3 days.</div>
<div class="alert error" role="alert">Payment failed.</div>
```

```css
.alert { padding: 12px 16px; border-radius: 12px; border-left: 4px solid; margin-bottom: 8px; }
.success { background: #f0fdf4; border-color: #16a34a; color: #166534; }
.warning { background: #fffbeb; border-color: #d97706; color: #92400e; }
.error { background: #fef2f2; border-color: #dc2626; color: #991b1b; }
```
