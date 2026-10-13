# HTML/CSS の例: アンカーへのスムーズスクロール

なめらかなスクロールと固定ヘッダー分の余白。

```html
<a href="#pricing">Pricing</a> … <section id="pricing">…</section>
```

```css
html { scroll-behavior: smooth; scroll-padding-top: 80px; }
@media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } }
```
