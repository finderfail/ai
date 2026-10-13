# CSS1：display、リスト、単位

**分類：**
```css
EM   { display: inline }         /* block | inline | list-item | none */
PRE  { white-space: pre }        /* normal | pre | nowrap */
UL   { list-style-type: disc }   /* disc circle square decimal lower-roman upper-roman lower-alpha upper-alpha none */
UL.img { list-style-image: url(dot.gif) }
OL   { list-style-position: inside }
UL   { list-style: square inside }
```

**長さの単位：**
- 相対：`em`（フォントサイズ）、`ex`（小文字の高さ）、`px`；
- 絶対：`in`、`cm`、`mm`、`pt`、`pc`；
- パーセント `%`。

**CSS1 時代の HTML でのスタイルの読み込み**：`<LINK REL=STYLESHEET HREF="style.css">`、`<HEAD>` 内の `<STYLE>` 要素、`STYLE` 属性、`@import url(style.css)`。

`rem`、`vw`、`vh` などの単位や `calc()` は CSS1 にない。
