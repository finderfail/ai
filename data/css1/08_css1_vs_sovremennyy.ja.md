# CSS1 と現代の CSS の違い

| やりたいこと | CSS1（1996年） | 現代の CSS |
|---|---|---|
| 段組み | `float` | flexbox、grid |
| 位置指定 | なし | `position`、`z-index` |
| ホバー | `:hover` なし | `:hover`、`:focus-visible` |
| 角丸、影 | なし | `border-radius`、`box-shadow` |
| 透明度 | なし | `opacity`、`rgba`、`/ alpha` |
| レスポンシブ | なし | メディアクエリ、`clamp()` |
| Web フォント | なし | `@font-face` |
| 変数 | なし | `--var`、`var()` |
| アニメーション | なし | `transition`、`@keyframes` |
| セレクター | タグ、クラス、ID、子孫 | `>`、`+`、`~`、属性、`:nth-child`、`:has()` |

ユーザーが「CSS1 で」コードを求めたら CSS1 の機能だけを使い、この規格は現代のサイトには使われないと伝えること。
