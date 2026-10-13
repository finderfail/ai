# HTML5: canvas и SVG

**canvas** — растровое рисование из JavaScript:
```html
<canvas id="c" width="300" height="150"></canvas>
<script>
  const ctx = document.getElementById('c').getContext('2d');
  ctx.fillStyle = '#7b5cff';
  ctx.fillRect(10, 10, 100, 50);
  ctx.beginPath();
  ctx.arc(200, 75, 40, 0, Math.PI * 2);
  ctx.fill();
  ctx.font = '16px sans-serif';
  ctx.fillText('Привет', 10, 120);
</script>
```

**SVG** — векторная графика прямо в HTML:
```html
<svg width="120" height="120" viewBox="0 0 120 120" role="img" aria-label="Логотип">
  <circle cx="60" cy="60" r="50" fill="#7b5cff"/>
  <path d="M40 60 L55 75 L85 45" stroke="#fff" stroke-width="8" fill="none"/>
</svg>
```

- SVG масштабируется без потери качества, стилизуется CSS и подходит для иконок и логотипов.
- canvas быстрее для большого числа объектов (игры, графики), но не доступен скринридерам.
