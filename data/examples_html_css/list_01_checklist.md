# Пример HTML/CSS: список с галочками

Маркеры-галочки вместо точек.

```html
<ul class="checks"><li>Fast</li><li>Secure</li><li>Simple</li></ul>
```

```css
.checks { list-style: none; padding: 0; }
.checks li { position: relative; padding-left: 28px; margin: 8px 0; }
.checks li::before { content: "✓"; position: absolute; left: 0; color: #16a34a; font-weight: 700; }
```
