# HTML/CSS の例: グラデーション文字

文字をグラデーションで塗る見出し。

```html
<h1 class="grad">Universal design</h1>
```

```css
.grad { background: linear-gradient(90deg, #8a5cff, #3fa2ff, #ff6bd6);
  -webkit-background-clip: text; background-clip: text; color: transparent;
  font-size: clamp(2rem, 6vw, 4rem); font-weight: 800; }
```
