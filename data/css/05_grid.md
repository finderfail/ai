# CSS: Grid

Grid — раскладка в **двух измерениях** (строки и колонки).

```css
.layout {
  display: grid;
  grid-template-columns: 250px 1fr;           /* сайдбар и основная часть */
  grid-template-rows: auto 1fr auto;
  grid-template-areas:
    "header header"
    "sidebar main"
    "footer footer";
  gap: 16px;
  min-height: 100vh;
}
.header  { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main    { grid-area: main; }

.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 12px;
}

.wide { grid-column: 1 / -1; }               /* на всю ширину */
.box  { grid-column: span 2; grid-row: 2 / 4; }
```

- `fr` — доля свободного места.
- `repeat(auto-fill, minmax(200px, 1fr))` — адаптивная сетка без медиазапросов.
- `place-items: center` — центрирование содержимого ячеек.
- Flexbox — для ряда элементов, Grid — для раскладки страницы и сеток.
