# Пример HTML/CSS: разделитель с текстом

Линия с надписью посередине («или»).

```html
<div class="or">or</div>
```

```css
.or { display: flex; align-items: center; gap: 12px; color: #9ca3af; font-size: 14px; }
.or::before, .or::after { content: ""; flex: 1; height: 1px; background: #e5e7eb; }
```
