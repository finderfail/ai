# HTML/CSS の例: 流れるテキスト

ロゴやテキストを無限にスクロール。

```html
<div class="marquee"><div class="track"><span>Fast · Secure · Simple · </span><span>Fast · Secure · Simple · </span></div></div>
```

```css
.marquee { overflow: hidden; white-space: nowrap; }
.track { display: inline-flex; animation: scroll 15s linear infinite; }
.track span { padding-right: 24px; }
@keyframes scroll { to { transform: translateX(-50%); } }
@media (prefers-reduced-motion: reduce) { .track { animation: none; } }
```
