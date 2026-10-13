# Пример HTML/CSS: мигающий курсор печати

Эффект печатной машинки на steps().

```html
<h2 class="type">Hello, world!</h2>
```

```css
.type { width: 13ch; white-space: nowrap; overflow: hidden; border-right: 3px solid;
  font-family: ui-monospace, monospace;
  animation: typing 2s steps(13), caret .7s step-end infinite alternate; }
@keyframes typing { from { width: 0; } }
@keyframes caret { 50% { border-color: transparent; } }
```
