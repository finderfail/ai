# Пример HTML/CSS: треугольник-стрелка на CSS

Стрелка у всплывающего блока через border.

```html
<div class="bubble">Hi!</div>
```

```css
.bubble { position: relative; display: inline-block; padding: 10px 14px; border-radius: 12px; background: #111; color: #fff; }
.bubble::after { content: ""; position: absolute; top: 100%; left: 20px;
  border: 8px solid transparent; border-top-color: #111; }
```
