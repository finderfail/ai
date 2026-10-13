# Пример HTML/CSS: горизонтальный список с разделителями

Пункты в строку через точки.

```html
<ul class="meta"><li>Oct 12</li><li>5 min read</li><li>CSS</li></ul>
```

```css
.meta { display: flex; flex-wrap: wrap; list-style: none; padding: 0; color: #6b7280; font-size: 14px; }
.meta li + li::before { content: "·"; margin: 0 8px; }
```
