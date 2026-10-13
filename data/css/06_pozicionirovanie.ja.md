# CSS：位置指定と z-index

```css
.static   { position: static; }     /* 既定。通常の流れ */
.relative { position: relative; top: 10px; }  /* 元の位置からずらす。流れの中の場所は残る */
.parent   { position: relative; }
.badge    { position: absolute; top: 0; right: 0; }  /* 最も近い位置指定済みの祖先が基準 */
.header   { position: fixed; top: 0; inset-inline: 0; } /* ウィンドウが基準。スクロールしない */
.toc      { position: sticky; top: 16px; } /* スクロール時に貼り付く */
```

- `absolute` は要素を流れから外す。`position` が `static` 以外の最も近い祖先が基準で、なければページが基準。
- `inset: 0` は `top: 0; right: 0; bottom: 0; left: 0` と同じ。
- 祖先に `overflow: hidden` があるか `top` がないと `sticky` は効かない。
- `z-index` は位置指定された要素（と flex/grid の子要素）だけに効く。**重ね合わせコンテキスト** の中で比較され、`opacity < 1`、`transform`、`filter`、`z-index` 付きの `position` が新しいコンテキストを作るため、`z-index: 9999` が「効かない」ことがある。
