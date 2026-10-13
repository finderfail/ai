# Пример HTML/CSS: стилизация ::marker

Цвет и форма маркеров стандартного списка.

```html
<ul class="fancy"><li>One</li><li>Two</li></ul>
```

```css
.fancy li::marker { color: #4f46e5; content: "▸ "; font-size: 1.1em; }
```
