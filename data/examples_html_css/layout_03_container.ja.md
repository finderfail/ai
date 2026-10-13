# HTML/CSS の例: 中央寄せコンテナ

左右に余白を持つ最大幅付きコンテナ。

```html
<div class="container">…</div>
```

```css
.container {
  width: min(100% - 32px, 1120px);
  margin-inline: auto;
}
```
