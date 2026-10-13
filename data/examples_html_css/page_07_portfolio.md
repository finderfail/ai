# Пример HTML/CSS: портфолио: сетка работ

Сетка проектов с подписями.

```html
<section class="works">
  <a href="#"><img src="w1.jpg" alt=""><span>Brand site</span></a>
  <a href="#"><img src="w2.jpg" alt=""><span>Mobile app</span></a>
</section>
```

```css
.works { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 20px; }
.works a { color: inherit; text-decoration: none; }
.works img { width: 100%; aspect-ratio: 4 / 3; object-fit: cover; border-radius: 14px; transition: transform .3s; }
.works a:hover img { transform: scale(1.02); }
.works span { display: block; margin-top: 8px; font-weight: 600; }
```
