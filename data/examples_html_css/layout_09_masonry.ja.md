# HTML/CSS の例: メイソンリー風レイアウト

column-count で高さの異なるカードを段組み。

```html
<div class="masonry"><div class="item">…</div><div class="item">…</div></div>
```

```css
.masonry { column-count: 3; column-gap: 16px; }
.item { break-inside: avoid; margin-bottom: 16px; padding: 16px; border-radius: 12px; background: #f3f4f6; }
@media (max-width: 900px) { .masonry { column-count: 2; } }
@media (max-width: 560px) { .masonry { column-count: 1; } }
```
