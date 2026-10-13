# HTML/CSS の例: ステップ表示

購入手続きのステップインジケーター。

```html
<ol class="steps">
  <li class="done">Cart</li><li class="current">Shipping</li><li>Payment</li><li>Done</li>
</ol>
```

```css
.steps { display: flex; gap: 8px; list-style: none; padding: 0; counter-reset: s; }
.steps li { flex: 1; padding-top: 10px; border-top: 4px solid #e5e7eb; color: #888; font-size: 14px; counter-increment: s; }
.steps li::before { content: counter(s) ". "; }
.steps .done { border-color: #4f46e5; color: #333; }
.steps .current { border-color: #a5b4fc; color: #111; font-weight: 600; }
```
