# CSS1: селекторы

```css
H1 { color: navy }                 /* по типу элемента */
H1, H2, H3 { font-family: serif }  /* группировка */
.note { color: red }               /* класс */
P.note { font-style: italic }
#intro { font-weight: bold }       /* ID */
UL LI { list-style: square }       /* контекстный (потомок) */

A:link    { color: blue }          /* непосещённая ссылка */
A:visited { color: purple }        /* посещённая */
A:active  { color: red }           /* активная (в момент клика) */

P:first-line   { font-variant: small-caps }
P:first-letter { font-size: 200%; float: left }
```

- В CSS1 псевдоклассы были **только у ссылок**: `:link`, `:visited`, `:active`. `:hover` и `:focus` появились в CSS2.
- Псевдоэлементы `:first-line` и `:first-letter` писались с одним двоеточием.
- Селекторов дочернего элемента (`>`), соседнего (`+`) и атрибутов (`[href]`) в CSS1 нет.
- Специфичность: (число ID, число классов и псевдоклассов, число тегов).
