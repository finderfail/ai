# HTML/CSS の例: ロゴの帯

横並びのロゴ。グレーで、hover でカラーに。

```html
<div class="logos"><img src="a.svg" alt="Acme"><img src="b.svg" alt="Globex"><img src="c.svg" alt="Initech"></div>
```

```css
.logos { display: flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: 40px; }
.logos img { height: 32px; filter: grayscale(1); opacity: .6; transition: filter .2s, opacity .2s; }
.logos img:hover { filter: none; opacity: 1; }
```
