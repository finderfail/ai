# Пример HTML/CSS: группа аватаров

Наложенные друг на друга аватары с счётчиком.

```html
<div class="avatars">
  <img src="1.jpg" alt="Ann"><img src="2.jpg" alt="Bob"><img src="3.jpg" alt="Kei"><span>+5</span>
</div>
```

```css
.avatars { display: flex; }
.avatars img, .avatars span { width: 36px; height: 36px; border-radius: 50%; border: 2px solid #fff;
  margin-left: -10px; object-fit: cover; }
.avatars > :first-child { margin-left: 0; }
.avatars span { display: grid; place-items: center; background: #e5e7eb; font-size: 12px; font-weight: 600; }
```
