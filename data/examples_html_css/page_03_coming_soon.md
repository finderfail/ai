# Пример HTML/CSS: страница «скоро запуск»

Заголовок и форма подписки по центру.

```html
<main class="soon"><h1>Coming soon</h1><p>We are launching next month.</p>
<form><input type="email" placeholder="you@mail.com" required><button>Notify me</button></form></main>
```

```css
.soon { min-height: 100dvh; display: grid; place-content: center; text-align: center; padding: 16px; }
.soon form { display: flex; gap: 8px; margin-top: 16px; }
.soon input { flex: 1; min-width: 0; padding: 10px 14px; border: 1px solid #ccc; border-radius: 10px; }
.soon button { padding: 10px 18px; border: 0; border-radius: 10px; background: #111; color: #fff; }
```
