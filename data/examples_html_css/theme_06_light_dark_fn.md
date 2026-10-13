# Пример HTML/CSS: функция light-dark()

Два цвета в одном значении для светлой и тёмной темы.

```html
<p class="note">Note</p>
```

```css
:root { color-scheme: light dark; }
.note { background: light-dark(#fef9c3, #3f3a12); color: light-dark(#713f12, #fde68a);
  padding: 12px 16px; border-radius: 10px; }
```
