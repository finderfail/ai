# Пример HTML/CSS: блоки с фиксированными пропорциями

Квадрат, 4:3 и 16:9 через aspect-ratio.

```html
<div class="square"></div><div class="photo"></div><div class="wide"></div>
```

```css
.square { aspect-ratio: 1; } .photo { aspect-ratio: 4 / 3; } .wide { aspect-ratio: 16 / 9; }
.square, .photo, .wide { width: 100%; background: #e5e7eb; border-radius: 12px; }
```
