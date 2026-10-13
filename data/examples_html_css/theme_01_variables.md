# Пример HTML/CSS: дизайн-токены на CSS-переменных

Цвета, отступы и радиусы в одном месте.

```html
<button class="btn">OK</button>
```

```css
:root {
  --color-bg: #ffffff; --color-text: #111827; --color-primary: #4f46e5;
  --space-2: 8px; --space-4: 16px; --radius: 12px;
}
body { background: var(--color-bg); color: var(--color-text); }
.btn { padding: var(--space-2) var(--space-4); border-radius: var(--radius);
  background: var(--color-primary); color: #fff; border: 0; }
```
