# HTML/CSS の例: 定義リスト

dl/dt/dd の2カラム表示。

```html
<dl class="specs"><dt>CPU</dt><dd>8 cores</dd><dt>RAM</dt><dd>32 GB</dd></dl>
```

```css
.specs { display: grid; grid-template-columns: max-content 1fr; gap: 8px 24px; }
.specs dt { color: #6b7280; }
.specs dd { margin: 0; font-weight: 600; }
```
