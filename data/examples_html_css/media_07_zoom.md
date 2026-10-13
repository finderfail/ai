# Пример HTML/CSS: увеличение картинки при наведении

Плавный zoom внутри рамки.

```html
<div class="zoom"><img src="photo.jpg" alt=""></div>
```

```css
.zoom { overflow: hidden; border-radius: 14px; }
.zoom img { display: block; width: 100%; transition: transform .4s ease; }
.zoom:hover img { transform: scale(1.08); }
```
