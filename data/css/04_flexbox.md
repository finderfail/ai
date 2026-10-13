# CSS: Flexbox

Flexbox — раскладка в **одном направлении** (строка или колонка).

```css
.container {
  display: flex;
  flex-direction: row;          /* row | column | row-reverse | column-reverse */
  justify-content: space-between; /* главная ось: center, flex-end, space-evenly… */
  align-items: center;          /* поперечная ось: stretch, flex-start, baseline… */
  flex-wrap: wrap;              /* перенос на новую строку */
  gap: 16px;                    /* расстояние между элементами */
}

.item { flex: 1; }              /* растягивается, делит место поровну */
.sidebar { flex: 0 0 250px; }   /* не растёт, не сжимается, база 250px */
.push-right { margin-left: auto; }
```

- `flex: <grow> <shrink> <basis>`; `flex: 1` = `1 1 0`.
- `justify-content` — вдоль `flex-direction`, `align-items` — поперёк.
- Центрирование по обеим осям: `display: flex; justify-content: center; align-items: center;`.
- Не сжимается элемент с длинным текстом — добавьте `min-width: 0`.
