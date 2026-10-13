# Пример HTML/CSS: кнопка с обводкой

Прозрачная кнопка с рамкой, заливается при наведении.

```html
<button class="btn-outline">Learn more</button>
```

```css
.btn-outline {
  padding: 10px 18px; border: 2px solid #4f46e5; border-radius: 10px;
  background: transparent; color: #4f46e5; font-weight: 600; cursor: pointer;
  transition: background .2s, color .2s;
}
.btn-outline:hover { background: #4f46e5; color: #fff; }
```
