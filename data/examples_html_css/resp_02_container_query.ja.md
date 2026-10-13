# HTML/CSS の例: コンテナクエリのカード

親コンテナの幅でカードの表示が変わる。

```html
<div class="slot"><article class="cq-card"><img src="a.jpg" alt=""><div>Text</div></article></div>
```

```css
.slot { container-type: inline-size; }
.cq-card { display: grid; gap: 12px; }
.cq-card img { width: 100%; border-radius: 10px; }
@container (min-width: 420px) {
  .cq-card { grid-template-columns: 160px 1fr; align-items: center; }
}
```
