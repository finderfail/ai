# HTML/CSS の例: reduced motion への配慮

OS で動きを減らす設定の人にはアニメを止める。

```html
<div class="animated">…</div>
```

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: .01ms !important; animation-iteration-count: 1 !important;
    transition-duration: .01ms !important; scroll-behavior: auto !important;
  }
}
```
