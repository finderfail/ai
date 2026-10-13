# Пример HTML/CSS: аккуратное кольцо фокуса

Видимый фокус только при навигации с клавиатуры.

```html
<button>Save</button><a href="#">Link</a>
```

```css
:focus { outline: none; }
:focus-visible { outline: 3px solid #a5b4fc; outline-offset: 2px; border-radius: 6px; }
```
