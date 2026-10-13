# Пример HTML/CSS: обрезка текста

Одна строка с многоточием и обрезка до 2 строк.

```html
<p class="one-line">Very long title…</p>
<p class="two-lines">Long description…</p>
```

```css
.one-line { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 260px; }
.two-lines { display: -webkit-box; -webkit-box-orient: vertical; -webkit-line-clamp: 2;
  line-clamp: 2; overflow: hidden; }
```
