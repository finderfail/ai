# Пример HTML/CSS: баннер cookie

Плашка внизу экрана с двумя кнопками.

```html
<div class="cookie" role="dialog" aria-label="Cookies">
  <p>We use cookies to improve the site.</p>
  <button>Decline</button><button class="primary">Accept</button>
</div>
```

```css
.cookie { position: fixed; left: 16px; right: 16px; bottom: 16px; display: flex; align-items: center; gap: 12px;
  flex-wrap: wrap; max-width: 640px; margin-inline: auto; padding: 16px; border-radius: 16px;
  background: #fff; box-shadow: 0 10px 40px rgb(0 0 0 / .15); }
.cookie p { flex: 1 1 240px; margin: 0; }
.cookie button { padding: 8px 14px; border-radius: 8px; border: 1px solid #ddd; background: #fff; }
.cookie .primary { background: #111; color: #fff; border-color: #111; }
```
