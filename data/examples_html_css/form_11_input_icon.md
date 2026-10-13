# Пример HTML/CSS: поле с иконкой и кнопкой

Поле пароля с кнопкой справа внутри.

```html
<div class="input-group">
  <input type="password" placeholder="Password">
  <button type="button" aria-label="Show password">👁</button>
</div>
```

```css
.input-group { position: relative; max-width: 320px; }
.input-group input { width: 100%; padding: 12px 44px 12px 14px; border: 1px solid #ccc; border-radius: 10px; }
.input-group button { position: absolute; right: 6px; top: 50%; transform: translateY(-50%);
  border: 0; background: none; cursor: pointer; padding: 6px; }
```
