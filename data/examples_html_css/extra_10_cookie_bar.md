# Пример HTML/CSS: плашка о cookies

Фиксированная плашка снизу с кнопками.

```html
<div class="cookie"><p>We use cookies to improve the site.</p><button class="ghost">Decline</button><button>Accept</button></div>
```

```css
.cookie { position: fixed; inset: auto 16px 16px; display: flex; flex-wrap: wrap; align-items: center; gap: 8px;
  max-width: 560px; margin: auto; padding: 14px 16px; border-radius: 14px; background: #111; color: #fff; }
.cookie p { flex: 1 1 220px; margin: 0; font-size: 14px; }
.cookie button { padding: 8px 14px; border: 0; border-radius: 8px; background: #fff; color: #111; }
.cookie .ghost { background: transparent; color: #fff; border: 1px solid #555; }
```
