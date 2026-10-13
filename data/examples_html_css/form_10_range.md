# Пример HTML/CSS: стилизованный range

Ползунок со своим цветом и бегунком.

```html
<input type="range" class="range" min="0" max="100" value="40">
```

```css
.range { width: 100%; accent-color: #4f46e5; }
.range::-webkit-slider-thumb { cursor: pointer; }
```
