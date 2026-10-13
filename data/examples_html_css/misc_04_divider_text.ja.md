# HTML/CSS の例: テキスト入りの区切り線

中央に文字のある線（「または」）。

```html
<div class="or">or</div>
```

```css
.or { display: flex; align-items: center; gap: 12px; color: #9ca3af; font-size: 14px; }
.or::before, .or::after { content: ""; flex: 1; height: 1px; background: #e5e7eb; }
```
