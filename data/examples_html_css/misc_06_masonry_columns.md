# Пример HTML/CSS: сетка «кирпичиками» на columns

Карточки разной высоты без пустот.

```html
<div class="masonry"><img src="1.jpg" alt=""><img src="2.jpg" alt=""><img src="3.jpg" alt=""></div>
```

```css
.masonry { columns: 3 240px; column-gap: 16px; }
.masonry > * { width: 100%; margin-bottom: 16px; break-inside: avoid; border-radius: 12px; }
```
