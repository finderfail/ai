# Пример HTML/CSS: полосатая таблица с подсветкой

Чередование строк и hover.

```html
<table class="zebra">…</table>
```

```css
.zebra { width: 100%; border-collapse: collapse; }
.zebra td, .zebra th { padding: 8px 12px; }
.zebra tbody tr:nth-child(even) { background: #f6f7f9; }
.zebra tbody tr:hover { background: #eef2ff; }
```
