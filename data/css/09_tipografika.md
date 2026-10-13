# CSS: типографика и шрифты

```css
body {
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  font-size: 1rem;
  line-height: 1.6;
  color: #1c1c1f;
}
h1 { font-size: clamp(2rem, 5vw, 3.5rem); font-weight: 700; letter-spacing: -0.02em; }
p  { max-width: 65ch; text-align: left; }
.caps { text-transform: uppercase; }
.ellipsis { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.clamp-3 { display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }

@font-face {
  font-family: "Inter";
  src: url("/fonts/Inter.woff2") format("woff2");
  font-weight: 100 900;
  font-display: swap;
}
```

- `line-height` без единиц (1.5–1.7) масштабируется вместе со шрифтом.
- `font-display: swap` показывает текст системным шрифтом, пока грузится свой.
- Формат шрифтов для веба — WOFF2.
