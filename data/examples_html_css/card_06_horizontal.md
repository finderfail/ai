# Пример HTML/CSS: горизонтальная карточка

Картинка слева, текст справа; на мобильном — колонкой.

```html
<article class="hcard">
  <img src="cover.jpg" alt="">
  <div><h3>How we scaled to 1M users</h3><p>Lessons from three years of growth.</p></div>
</article>
```

```css
.hcard { display: flex; gap: 16px; max-width: 640px; padding: 12px; border-radius: 16px; background: #fff;
  box-shadow: 0 2px 12px rgb(0 0 0 / .06); }
.hcard img { width: 180px; aspect-ratio: 4 / 3; object-fit: cover; border-radius: 10px; flex-shrink: 0; }
.hcard h3 { margin: 4px 0 8px; }
@media (max-width: 560px) { .hcard { flex-direction: column; } .hcard img { width: 100%; } }
```
