# HTML/CSS の例: テキスト付き区切り線

中央に「または」のある線。

```html
<div class="divider">or</div>
```

```css
.divider { display: flex; align-items: center; gap: 12px; color: #888; font-size: 14px; }
.divider::before, .divider::after { content: ""; flex: 1; height: 1px; background: #e5e7eb; }
```
