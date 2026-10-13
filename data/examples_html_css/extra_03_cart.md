# Пример HTML/CSS: итог корзины

Строки сумм и кнопка оформления.

```html
<aside class="summary"><div><span>Subtotal</span><span>$129</span></div><div><span>Shipping</span><span>Free</span></div>
<div class="total"><span>Total</span><span>$129</span></div><button>Checkout</button></aside>
```

```css
.summary { display: grid; gap: 10px; padding: 20px; border-radius: 16px; background: #f9fafb; max-width: 360px; }
.summary div { display: flex; justify-content: space-between; font-variant-numeric: tabular-nums; }
.total { padding-top: 10px; border-top: 1px solid #e5e7eb; font-weight: 700; font-size: 18px; }
.summary button { margin-top: 8px; padding: 12px; border: 0; border-radius: 10px; background: #16a34a; color: #fff; }
```
