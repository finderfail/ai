# CSS1: display, списки, единицы

**Классификация:**
```css
EM   { display: inline }         /* block | inline | list-item | none */
PRE  { white-space: pre }        /* normal | pre | nowrap */
UL   { list-style-type: disc }   /* disc circle square decimal lower-roman upper-roman lower-alpha upper-alpha none */
UL.img { list-style-image: url(dot.gif) }
OL   { list-style-position: inside }
UL   { list-style: square inside }
```

**Единицы длины:**
- относительные: `em` (размер шрифта), `ex` (высота строчной буквы), `px`;
- абсолютные: `in`, `cm`, `mm`, `pt`, `pc`;
- проценты `%`.

**Подключение стилей в HTML** во времена CSS1: `<LINK REL=STYLESHEET HREF="style.css">`, элемент `<STYLE>` в `<HEAD>`, атрибут `STYLE`, а также `@import url(style.css)`.

Единиц `rem`, `vw`, `vh` и функции `calc()` в CSS1 нет.
