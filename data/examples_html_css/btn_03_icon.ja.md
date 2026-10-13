# HTML/CSS の例: アイコンボタン

SVG アイコンとスクリーンリーダー用ラベル付きの丸いボタン。

```html
<button class="icon-btn" aria-label="Close">
  <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true">
    <path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
  </svg>
</button>
```

```css
.icon-btn {
  width: 40px; height: 40px; border-radius: 50%; border: 0;
  display: inline-grid; place-items: center;
  background: #f1f2f5; color: #333; cursor: pointer;
}
.icon-btn:hover { background: #e4e5e9; }
```
