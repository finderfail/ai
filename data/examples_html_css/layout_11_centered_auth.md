# Пример HTML/CSS: страница входа по центру

Форма входа по центру экрана с фоном.

```html
<main class="auth-page"><form class="auth-card">…</form></main>
```

```css
.auth-page { min-height: 100vh; display: grid; place-items: center; padding: 16px;
  background: radial-gradient(1200px 600px at 50% -10%, #eef2ff, transparent 70%), #fff; }
.auth-card { width: min(100%, 380px); padding: 32px; border-radius: 24px; background: #fff;
  border: 1px solid #e5e7eb; box-shadow: 0 10px 40px rgb(0 0 0 / .08); }
```
