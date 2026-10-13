# HTML/CSS の例: 横スクロールする広い表

スマホのレイアウトを崩さない表。

```html
<div class="x-scroll"><table class="wide">…</table></div>
```

```css
.x-scroll { overflow-x: auto; -webkit-overflow-scrolling: touch; }
.wide { min-width: 720px; border-collapse: collapse; }
.wide th, .wide td { white-space: nowrap; padding: 8px 12px; }
```
