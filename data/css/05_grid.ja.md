# CSS：Grid

Grid は **2次元**（行と列）のレイアウト。

```css
.layout {
  display: grid;
  grid-template-columns: 250px 1fr;           /* サイドバーとメイン */
  grid-template-rows: auto 1fr auto;
  grid-template-areas:
    "header header"
    "sidebar main"
    "footer footer";
  gap: 16px;
  min-height: 100vh;
}
.header  { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main    { grid-area: main; }

.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 12px;
}

.wide { grid-column: 1 / -1; }               /* 全幅 */
.box  { grid-column: span 2; grid-row: 2 / 4; }
```

- `fr` は空きスペースの割合。
- `repeat(auto-fill, minmax(200px, 1fr))` はメディアクエリなしのレスポンシブなグリッド。
- `place-items: center` でセルの内容を中央寄せ。
- 要素の並びには Flexbox、ページのレイアウトやグリッドには Grid。
