# Пример HTML/CSS: mobile-first сетка

Одна колонка на телефоне, 2 и 4 на больших экранах.

```html
<div class="products">…</div>
```

```css
.products { display: grid; gap: 16px; grid-template-columns: 1fr; }
@media (min-width: 640px) { .products { grid-template-columns: repeat(2, 1fr); } }
@media (min-width: 1024px) { .products { grid-template-columns: repeat(4, 1fr); } }
```
