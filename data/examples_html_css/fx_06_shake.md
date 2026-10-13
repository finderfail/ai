# Пример HTML/CSS: тряска при ошибке

Поле трясётся при неверном вводе.

```html
<input class="shake" aria-invalid="true">
```

```css
.shake[aria-invalid="true"] { border-color: #dc2626; animation: shake .4s; }
@keyframes shake { 20%, 60% { transform: translateX(-6px); } 40%, 80% { transform: translateX(6px); } }
```
