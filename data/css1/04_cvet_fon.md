# CSS1: цвет и фон

```css
BODY {
  color: black;
  background-color: white;
  background-image: url(paper.gif);
  background-repeat: repeat-y;        /* repeat | repeat-x | repeat-y | no-repeat */
  background-attachment: fixed;       /* scroll | fixed */
  background-position: top center;    /* ключевые слова, % или длины */
}
H1 { background: #CCCCFF url(logo.gif) no-repeat }   /* сокращённая запись */
```

**Цвета в CSS1:**
- 16 названий цветов: aqua, black, blue, fuchsia, gray, green, lime, maroon, navy, olive, purple, red, silver, teal, white, yellow;
- `#RGB` и `#RRGGBB`: `#F00`, `#FF0000`;
- `rgb(255, 0, 0)` и `rgb(100%, 0%, 0%)`.

Прозрачности (`rgba`, `opacity`), градиентов и нескольких фонов в CSS1 нет.
