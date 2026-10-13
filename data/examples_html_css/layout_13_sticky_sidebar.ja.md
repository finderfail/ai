# HTML/CSS の例: スティッキーサイドバー

記事のスクロール中に目次が貼り付く。

```html
<div class="doc"><article>Long text…</article><aside class="toc">On this page</aside></div>
```

```css
.doc { display: grid; grid-template-columns: 1fr 240px; gap: 32px; align-items: start; }
.toc { position: sticky; top: 80px; max-height: calc(100vh - 100px); overflow: auto; }
@media (max-width: 900px) { .doc { grid-template-columns: 1fr; } .toc { position: static; } }
```
