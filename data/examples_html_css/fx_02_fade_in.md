# Пример HTML/CSS: плавное появление

Элементы появляются снизу при загрузке, с задержками.

```html
<h1 class="reveal">Hello</h1><p class="reveal" style="--d: .15s">World</p>
```

```css
.reveal { animation: reveal .6s ease-out both; animation-delay: var(--d, 0s); }
@keyframes reveal { from { opacity: 0; transform: translateY(16px); } }
@media (prefers-reduced-motion: reduce) { .reveal { animation: none; } }
```
