# Пример HTML/CSS: picture с форматами и темой

Разные картинки для тёмной темы и современных форматов.

```html
<picture>
  <source srcset="logo-dark.svg" media="(prefers-color-scheme: dark)">
  <source srcset="hero.avif" type="image/avif">
  <img src="hero.jpg" alt="Hero image" width="1200" height="600">
</picture>
```

```css
picture img { max-width: 100%; height: auto; display: block; }
```
