# HTML/CSS の例: 暗いオーバーレイ付き背景画像

テキストの下にグラデーションの暗幕を敷いた背景写真。

```html
<section class="banner"><h2>Explore Japan</h2></section>
```

```css
.banner { display: grid; align-items: end; min-height: 360px; padding: 32px; color: #fff; border-radius: 20px;
  background: linear-gradient(to top, rgb(0 0 0 / .7), transparent 60%), url(tokyo.jpg) center / cover; }
.banner h2 { margin: 0; font-size: 2rem; }
```
