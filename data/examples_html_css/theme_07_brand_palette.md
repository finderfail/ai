# Пример HTML/CSS: палитра оттенков через color-mix

Светлые и тёмные оттенки из одного фирменного цвета.

```html
<div class="chip">Brand</div>
```

```css
:root { --brand: #4f46e5;
  --brand-100: color-mix(in srgb, var(--brand) 12%, white);
  --brand-700: color-mix(in srgb, var(--brand) 80%, black); }
.chip { background: var(--brand-100); color: var(--brand-700); padding: 4px 12px; border-radius: 999px; }
```
