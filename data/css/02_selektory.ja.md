# CSS：セレクター

```css
p { }                    /* タグ */
.card { }                /* クラス */
#header { }              /* id */
* { }                    /* すべての要素 */
nav a { }                /* 子孫 */
ul > li { }              /* 直接の子 */
h2 + p { }               /* 直後の兄弟 */
h2 ~ p { }               /* 後続のすべての兄弟 */
a[href] { }              /* 属性がある */
a[href^="https"] { }     /* 前方一致 */
a[href$=".pdf"] { }      /* 後方一致 */
img[alt*="logo"] { }     /* 部分一致 */
li:first-child, li:last-child { }
li:nth-child(2n+1) { }   /* 奇数番目 */
input:not([disabled]) { }
:is(h1, h2, h3) a { }    /* グループ化、詳細度は最も強いもの */
:where(.btn) { }         /* 詳細度ゼロのグループ化 */
.card:has(img) { }       /* img を含む親 */
```

カンマでグループ化：`h1, h2 { margin: 0; }`。属性セレクター、`:nth-child`、`:not`、`~` は CSS3（Selectors Level 3）で追加。`:is`、`:where`、`:has` は Selectors Level 4 で、現在の主要ブラウザはすべて対応。
