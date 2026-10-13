# Пример HTML/CSS: подъём карточки при наведении

Карточка поднимается и тень усиливается.

```html
<article class="lift">…</article>
```

```css
.lift { transition: transform .2s ease, box-shadow .2s ease; border-radius: 16px; background: #fff;
  box-shadow: 0 2px 8px rgb(0 0 0 / .06); }
.lift:hover { transform: translateY(-4px); box-shadow: 0 12px 28px rgb(0 0 0 / .12); }
```
