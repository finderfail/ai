# Пример HTML/CSS: превью одинакового размера

Квадратные превью из картинок разных пропорций.

```html
<img class="thumb" src="any.jpg" alt="">
```

```css
.thumb { width: 120px; height: 120px; object-fit: cover; object-position: center; border-radius: 12px; }
```
