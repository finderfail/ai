# Пример HTML/CSS: круговой прогресс

Кольцо прогресса на conic-gradient.

```html
<div class="ring" style="--p: 72" role="progressbar" aria-valuenow="72">72%</div>
```

```css
.ring { width: 96px; aspect-ratio: 1; display: grid; place-items: center; border-radius: 50%; font-weight: 700;
  background: radial-gradient(closest-side, #fff 78%, transparent 80%),
              conic-gradient(#4f46e5 calc(var(--p) * 1%), #e5e7eb 0); }
```
