# Пример HTML/CSS: три точки загрузки

Индикатор «печатает…».

```html
<span class="dots" aria-label="Loading"><i></i><i></i><i></i></span>
```

```css
.dots { display: inline-flex; gap: 4px; }
.dots i { width: 8px; height: 8px; border-radius: 50%; background: #9ca3af; animation: dot 1s infinite ease-in-out; }
.dots i:nth-child(2) { animation-delay: .15s; } .dots i:nth-child(3) { animation-delay: .3s; }
@keyframes dot { 0%, 80%, 100% { opacity: .3; transform: scale(.8); } 40% { opacity: 1; transform: none; } }
```
