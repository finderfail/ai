# Пример HTML/CSS: блик на кнопке

Световой блик пробегает по кнопке при наведении.

```html
<button class="shine">Buy now</button>
```

```css
.shine { position: relative; overflow: hidden; padding: 12px 22px; border: 0; border-radius: 10px; background: #111; color: #fff; }
.shine::after { content: ""; position: absolute; top: 0; left: -60%; width: 40%; height: 100%;
  background: linear-gradient(120deg, transparent, rgb(255 255 255 / .35), transparent); transform: skewX(-20deg); }
.shine:hover::after { left: 120%; transition: left .6s; }
```
