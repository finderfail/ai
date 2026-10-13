# Пример HTML/CSS: неактивная кнопка

Стили для disabled-кнопки и ссылки-кнопки.

```html
<button class="btn" disabled>Submit</button>
<a class="btn" aria-disabled="true">Next</a>
```

```css
.btn { padding: 10px 18px; border: 0; border-radius: 8px; background: #4f46e5; color: #fff; }
.btn:disabled, .btn[aria-disabled="true"] {
  background: #c7c9d1; color: #6b6e78; cursor: not-allowed; pointer-events: none;
}
```
