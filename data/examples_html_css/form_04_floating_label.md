# Пример HTML/CSS: плавающая подпись поля

Подпись поднимается над полем при вводе.

```html
<div class="field">
  <input id="name" placeholder=" ">
  <label for="name">Full name</label>
</div>
```

```css
.field { position: relative; }
.field input { width: 100%; padding: 20px 12px 8px; border: 1px solid #ccc; border-radius: 10px; font: inherit; }
.field label { position: absolute; left: 12px; top: 14px; color: #888; transition: .15s; pointer-events: none; }
.field input:focus + label,
.field input:not(:placeholder-shown) + label { top: 4px; font-size: 12px; color: #4f46e5; }
```
