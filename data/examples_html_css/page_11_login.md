# Пример HTML/CSS: страница входа

Карточка формы по центру экрана.

```html
<main class="auth"><form class="auth-card"><h1>Sign in</h1>
<input type="email" placeholder="Email" autocomplete="email" required>
<input type="password" placeholder="Password" autocomplete="current-password" required>
<button>Sign in</button><a href="/signup">Create account</a></form></main>
```

```css
.auth { min-height: 100dvh; display: grid; place-items: center; background: #f3f4f6; padding: 16px; }
.auth-card { width: min(100%, 380px); display: grid; gap: 12px; padding: 32px; background: #fff; border-radius: 20px; box-shadow: 0 10px 40px rgb(0 0 0 / .08); }
.auth-card input { padding: 12px; border: 1px solid #d1d5db; border-radius: 10px; }
.auth-card button { padding: 12px; border: 0; border-radius: 10px; background: #111; color: #fff; }
.auth-card a { text-align: center; font-size: 14px; }
```
