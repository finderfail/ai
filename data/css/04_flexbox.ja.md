# CSS：Flexbox

Flexbox は **1方向**（行または列）のレイアウト。

```css
.container {
  display: flex;
  flex-direction: row;          /* row | column | row-reverse | column-reverse */
  justify-content: space-between; /* 主軸：flex-start | center | flex-end | space-around | space-evenly */
  align-items: center;          /* 交差軸：stretch | flex-start | center | flex-end | baseline */
  flex-wrap: wrap;              /* 折り返し */
  gap: 16px;                    /* 要素間の間隔 */
}

.item { flex: 1; }              /* 伸びて均等に分ける */
.sidebar { flex: 0 0 250px; }   /* 伸びず縮まず、基準 250px */
.push-right { margin-left: auto; }
```

- `flex: <grow> <shrink> <basis>`。`flex: 1` は `1 1 0`。
- `justify-content` は `flex-direction` の方向、`align-items` はそれと直角の方向。
- 両方向の中央寄せ：`display: flex; justify-content: center; align-items: center;`。
- 長い文字列を含む要素が縮まないときは `min-width: 0` を追加。
