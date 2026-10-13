# Пример HTML/CSS: обрезка текста многоточием

Одна строка и несколько строк.

```html
<p class="one">Very long title…</p><p class="three">Long description…</p>
```

```css
.one { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.three { display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }
```
