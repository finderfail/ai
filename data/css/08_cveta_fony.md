# CSS: цвета, фоны, рамки, тени

**Цвета:** `red`, `#7b5cff`, `#7b5cff80` (с прозрачностью), `rgb(123 92 255 / 0.5)`, `hsl(255 100% 68%)`, `oklch(65% 0.2 285)`, `transparent`, `currentColor`.

```css
.card {
  background-color: #fff;
  background-image: url("bg.png");
  background-size: cover;            /* contain — целиком вписать */
  background-position: center;
  background-repeat: no-repeat;
  border: 1px solid #e3e4e8;
  border-radius: 16px;               /* скругление; 50% — круг */
  box-shadow: 0 4px 24px rgb(0 0 0 / 0.08);
  opacity: 0.9;
}
.hero {
  background: linear-gradient(135deg, #8a5cff, #5b6bff);
}
.badge {
  background: radial-gradient(circle, #fff 0%, transparent 70%);
}
h1 { text-shadow: 0 2px 4px rgb(0 0 0 / 0.3); }
.outline { outline: 2px solid #7b5cff; outline-offset: 2px; }
```

- Скругления, тени, градиенты, RGBA — возможности CSS3.
- `opacity` делает прозрачным весь элемент с содержимым; для прозрачного только фона используйте цвет с альфа-каналом.
