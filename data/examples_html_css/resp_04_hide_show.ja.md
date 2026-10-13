# HTML/CSS の例: 幅で表示切り替え

スマホとデスクトップで別の要素を表示。

```html
<span class="mobile-only">Menu</span><nav class="desktop-only">…</nav>
```

```css
.mobile-only { display: none; }
@media (max-width: 768px) {
  .mobile-only { display: inline; }
  .desktop-only { display: none; }
}
```
