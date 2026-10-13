# HTML/CSS の例: リンクの下線アニメーション

hover で下線が左から右へ伸びる。

```html
<a class="link" href="#">Read more</a>
```

```css
.link { color: #111; text-decoration: none;
  background: linear-gradient(currentColor, currentColor) 0 100% / 0 2px no-repeat;
  transition: background-size .3s; }
.link:hover { background-size: 100% 2px; }
```
