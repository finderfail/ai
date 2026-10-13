# Пример HTML/CSS: адаптивная галерея

Сетка изображений без медиазапросов.

```html
<div class="gallery">
  <img src="1.jpg" alt=""><img src="2.jpg" alt=""><img src="3.jpg" alt=""><img src="4.jpg" alt="">
</div>
```

```css
.gallery { display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 8px; }
.gallery img { width: 100%; aspect-ratio: 1; object-fit: cover; border-radius: 8px; display: block; }
```
