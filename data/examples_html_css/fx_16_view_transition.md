# Пример HTML/CSS: плавная смена страниц

Переход между страницами сайта без JS (View Transitions).

```html
<a href="/about">About</a>
```

```css
@view-transition { navigation: auto; }
::view-transition-old(root), ::view-transition-new(root) { animation-duration: .25s; }
```
