# HTML/CSS の例: 印刷用スタイル

ナビを隠しリンク先 URL を表示。

```html
<nav>…</nav><article><a href="https://example.com">Docs</a></article>
```

```css
@media print {
  nav, footer, .no-print { display: none !important; }
  body { color: #000; background: #fff; font-size: 12pt; }
  a[href^="http"]::after { content: " (" attr(href) ")"; font-size: 10pt; }
  h2, h3 { break-after: avoid; } img, table { break-inside: avoid; }
}
```
