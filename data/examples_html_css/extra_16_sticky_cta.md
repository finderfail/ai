# Пример HTML/CSS: липкая кнопка действия на мобильном

Кнопка «купить» прибита к низу экрана.

```html
<div class="cta-bar"><span>$129</span><button>Buy now</button></div>
```

```css
.cta-bar { position: sticky; bottom: 0; display: flex; justify-content: space-between; align-items: center;
  padding: 12px 16px calc(12px + env(safe-area-inset-bottom)); background: #fff; border-top: 1px solid #e5e7eb; }
.cta-bar button { padding: 12px 24px; border: 0; border-radius: 12px; background: #111; color: #fff; }
@media (min-width: 900px) { .cta-bar { display: none; } }
```
