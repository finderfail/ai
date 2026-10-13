# HTML/CSS の例: 料金プランカード

価格、機能リスト、おすすめプランの強調。

```html
<div class="plan featured">
  <h3>Pro</h3><p class="price">$12<span>/mo</span></p>
  <ul><li>Unlimited projects</li><li>Priority support</li><li>API access</li></ul>
  <button>Upgrade</button>
</div>
```

```css
.plan { width: 260px; padding: 28px; border: 1px solid #e3e4e8; border-radius: 20px; background: #fff; }
.plan.featured { border-color: #4f46e5; box-shadow: 0 0 0 4px #e0e7ff; }
.price { font-size: 40px; font-weight: 800; margin: 8px 0; }
.price span { font-size: 16px; font-weight: 400; color: #777; }
.plan ul { padding-left: 18px; color: #444; line-height: 1.8; }
.plan button { width: 100%; padding: 12px; border: 0; border-radius: 10px; background: #4f46e5; color: #fff; }
```
