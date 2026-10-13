# Пример HTML/CSS: тонкий скроллбар

Стилизация полосы прокрутки.

```html
<div class="scroll-area">…</div>
```

```css
.scroll-area { overflow: auto; scrollbar-width: thin; scrollbar-color: #c4c4cc transparent; }
.scroll-area::-webkit-scrollbar { width: 8px; }
.scroll-area::-webkit-scrollbar-thumb { background: #c4c4cc; border-radius: 4px; }
```
