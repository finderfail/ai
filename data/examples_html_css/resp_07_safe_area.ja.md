# HTML/CSS の例: 画面のノッチ対応の余白

スマホのノッチや角丸を考慮する。

```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
```

```css
body {
  padding: env(safe-area-inset-top) env(safe-area-inset-right)
           env(safe-area-inset-bottom) env(safe-area-inset-left);
}
.bottom-bar { padding-bottom: calc(12px + env(safe-area-inset-bottom)); }
```
