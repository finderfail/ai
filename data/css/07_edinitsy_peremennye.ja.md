# CSS：単位、calc()、変数

**単位：**
- `px`：CSS ピクセル；
- `%`：親のサイズに対する割合；
- `em`：要素のフォントサイズ基準（`font-size` 内では親が基準）；
- `rem`：ルート `html` のフォントサイズ基準（通常16px）。レスポンシブな余白や文字に便利；
- `vw`、`vh`：ウィンドウ幅・高さの1%。`dvh`、`svh`、`lvh` はモバイルのブラウザバーを考慮；
- `ch`：「0」の文字幅。本文の幅に便利：`max-width: 65ch`；
- `fr`：Grid での割合。

**関数：**
```css
.box { width: calc(100% - 2rem); }
h1 { font-size: clamp(1.5rem, 4vw, 3rem); }   /* 最小、推奨、最大 */
.col { width: min(100%, 700px); }
```

**カスタムプロパティ（変数）：**
```css
:root {
  --brand: #7b5cff;
  --gap: 16px;
}
.button { background: var(--brand); padding: var(--gap, 12px); }
@media (prefers-color-scheme: dark) { :root { --brand: #9c84ff; } }
```
変数は継承され、メディアクエリや JavaScript でも変更できる：`el.style.setProperty('--brand', 'red')`。
