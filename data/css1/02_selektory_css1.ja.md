# CSS1：セレクター

```css
H1 { color: navy }                 /* 要素の種類 */
H1, H2, H3 { font-family: serif }  /* グループ化 */
.note { color: red }               /* クラス */
P.note { font-style: italic }
#intro { font-weight: bold }       /* ID */
UL LI { list-style: square }       /* 文脈（子孫） */

A:link    { color: blue }          /* 未訪問のリンク */
A:visited { color: purple }        /* 訪問済み */
A:active  { color: red }           /* アクティブ（クリック中） */

P:first-line   { font-variant: small-caps }
P:first-letter { font-size: 200%; float: left }
```

- CSS1 の疑似クラスは **リンクだけ**：`:link`、`:visited`、`:active`。`:hover` と `:focus` は CSS2 で追加。
- 疑似要素 `:first-line` と `:first-letter` はコロン1つで書いた。
- 子（`>`）、隣接（`+`）、属性（`[href]`）のセレクターは CSS1 にない。
- 詳細度：（ID の数、クラスと疑似クラスの数、タグの数）。
