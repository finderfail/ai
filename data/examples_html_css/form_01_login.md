# Пример HTML/CSS: форма входа

Почта, пароль, «запомнить меня» и кнопка.

```html
<form class="form">
  <label>Email<input type="email" name="email" required autocomplete="email"></label>
  <label>Password<input type="password" name="password" required autocomplete="current-password"></label>
  <label class="check"><input type="checkbox" name="remember"> Remember me</label>
  <button type="submit">Sign in</button>
</form>
```

```css
.form { display: grid; gap: 14px; width: min(100%, 360px); }
.form label { display: grid; gap: 6px; font-size: 14px; font-weight: 600; }
.form input:not([type="checkbox"]) { padding: 12px 14px; border: 1px solid #d0d3da; border-radius: 10px; font: inherit; }
.form input:focus { outline: 2px solid #a5b4fc; border-color: #4f46e5; }
.check { display: flex !important; align-items: center; gap: 8px; font-weight: 400 !important; }
.form button { padding: 12px; border: 0; border-radius: 10px; background: #4f46e5; color: #fff; font-weight: 600; }
```
