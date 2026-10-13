# CSS1：ボックスモデルと float

```css
P {
  margin: 1em 2em;                       /* margin-top/right/bottom/left */
  padding: 0.5em;
  border-width: thin;                    /* thin | medium | thick | 長さ */
  border-style: solid;                   /* none dotted dashed solid double groove ridge inset outset */
  border-color: gray;
  width: 50%;
  height: auto;
}
IMG.left  { float: left; margin-right: 1em }
DIV.after { clear: both }                /* left | right | both | none */
H2 { border-bottom: thin solid black }
```

- `width` と `height` は **内容** のサイズで、padding と border はその外側に加わる（content-box の動作）。
- 隣接するブロックの上下マージンは相殺される。
- CSS1 で段組みをする唯一の方法は `float`。位置指定（`position`）はまだなかった。
- 枠線スタイル `dotted` 〜 `outset` は CSS1 に定義されていたが、当時のブラウザは一部しか対応していなかった。
