# Пример HTML/CSS: резиновая типографика

Размеры шрифтов плавно масштабируются через clamp().

```html
<h1>Fluid heading</h1><p>Body text</p>
```

```css
:root { font-size: clamp(16px, 0.9rem + 0.3vw, 18px); }
h1 { font-size: clamp(2rem, 1.2rem + 3vw, 3.75rem); line-height: 1.1; }
h2 { font-size: clamp(1.5rem, 1.1rem + 1.5vw, 2.5rem); }
```
