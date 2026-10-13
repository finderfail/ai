# HTML/CSS の例: 登録フォーム

パスワードのヒントと同意付きの登録フォーム。

```html
<form class="form">
  <label>Email<input type="email" required></label>
  <label>Password<input type="password" minlength="8" required aria-describedby="ph"></label>
  <small id="ph">At least 8 characters</small>
  <label class="check"><input type="checkbox" required> I accept the terms</label>
  <button>Create account</button>
</form>
```

```css
.form { display: grid; gap: 12px; max-width: 360px; }
.form label { display: grid; gap: 6px; }
.form input:not([type="checkbox"]) { padding: 12px; border: 1px solid #ccc; border-radius: 10px; }
.form small { color: #777; margin-top: -6px; }
.check { display: flex !important; gap: 8px; }
.form button { padding: 12px; border: 0; border-radius: 10px; background: #111; color: #fff; }
```
