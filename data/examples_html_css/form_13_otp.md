# Пример HTML/CSS: поля для кода из СМС

Шесть ячеек для одноразового кода.

```html
<div class="otp">
  <input inputmode="numeric" maxlength="1" autocomplete="one-time-code"><input inputmode="numeric" maxlength="1">
  <input inputmode="numeric" maxlength="1"><input inputmode="numeric" maxlength="1">
  <input inputmode="numeric" maxlength="1"><input inputmode="numeric" maxlength="1">
</div>
```

```css
.otp { display: flex; gap: 8px; }
.otp input { width: 48px; height: 56px; text-align: center; font-size: 24px; border: 1px solid #ccc; border-radius: 10px; }
.otp input:focus { outline: 2px solid #4f46e5; }
```
