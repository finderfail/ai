# HTML/CSS の例: ドキュメントのレイアウト

サイドメニュー、本文、右の目次。

```html
<div class="docs"><nav class="side">…</nav><main class="doc">…</main><aside class="toc">…</aside></div>
```

```css
.docs { display: grid; grid-template-columns: 240px minmax(0, 1fr) 200px; gap: 32px; max-width: 1280px; margin: auto; }
.side, .toc { position: sticky; top: 16px; align-self: start; max-height: calc(100dvh - 32px); overflow: auto; }
.doc { max-width: 75ch; }
@media (max-width: 1100px) { .docs { grid-template-columns: 220px minmax(0, 1fr); } .toc { display: none; } }
@media (max-width: 760px) { .docs { grid-template-columns: 1fr; } .side { position: static; } }
```
