# Пример HTML/CSS: индикатор прогресса

Полоса прогресса на элементе progress.

```html
<label>Upload <progress class="bar" value="65" max="100">65%</progress></label>
```

```css
.bar { width: 100%; height: 10px; appearance: none; border: 0; border-radius: 999px; overflow: hidden; background: #e5e7eb; }
.bar::-webkit-progress-bar { background: #e5e7eb; }
.bar::-webkit-progress-value { background: linear-gradient(90deg, #8a5cff, #3fa2ff); border-radius: 999px; }
.bar::-moz-progress-bar { background: linear-gradient(90deg, #8a5cff, #3fa2ff); }
```
