# Пример HTML/CSS: скрыть визуально, оставить для скринридеров

Класс sr-only.

```html
<button><svg aria-hidden="true">…</svg><span class="sr-only">Close</span></button>
```

```css
.sr-only { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0; }
```
