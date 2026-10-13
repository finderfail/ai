# Пример HTML/CSS: рейтинг звёздами

Отображение оценки 4.5 из 5 через градиент.

```html
<div class="stars" style="--rating: 4.5" role="img" aria-label="Rated 4.5 out of 5"></div>
```

```css
.stars { --percent: calc(var(--rating) / 5 * 100%); display: inline-block; font-size: 24px; line-height: 1; }
.stars::before { content: "★★★★★"; letter-spacing: 2px;
  background: linear-gradient(90deg, #f59e0b var(--percent), #d1d5db var(--percent));
  -webkit-background-clip: text; background-clip: text; color: transparent; }
```
