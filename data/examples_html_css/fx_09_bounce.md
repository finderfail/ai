# Пример HTML/CSS: прыгающая стрелка вниз

Подсказка «листайте вниз».

```html
<a class="scroll-hint" href="#next" aria-label="Scroll down">↓</a>
```

```css
.scroll-hint { display: inline-block; font-size: 28px; text-decoration: none; animation: bounce 1.6s infinite; }
@keyframes bounce { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(8px); } }
```
