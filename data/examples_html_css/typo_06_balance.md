# Пример HTML/CSS: ровные переносы заголовков

text-wrap: balance и pretty для красивых строк.

```html
<h2 class="balanced">A heading that wraps across two lines nicely</h2>
```

```css
h1, h2, h3 { text-wrap: balance; }
p { text-wrap: pretty; }
.balanced { max-width: 22ch; }
```
