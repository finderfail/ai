# Пример HTML/CSS: анимированный градиентный фон

Переливающийся фон секции.

```html
<section class="aurora">…</section>
```

```css
.aurora { min-height: 300px; background: linear-gradient(120deg, #8a5cff, #3fa2ff, #ff6bd6, #8a5cff);
  background-size: 300% 300%; animation: flow 12s ease infinite; }
@keyframes flow { 50% { background-position: 100% 50%; } }
```
