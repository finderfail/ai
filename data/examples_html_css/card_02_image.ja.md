# HTML/CSS の例: 画像付きカード

上に object-fit の画像、下にテキスト。

```html
<article class="card">
  <img src="photo.jpg" alt="Mountain lake">
  <div class="card-body"><h3>Lake Bled</h3><p>Slovenia · 5 days</p></div>
</article>
```

```css
.card { width: 300px; border-radius: 16px; overflow: hidden; background: #fff;
  box-shadow: 0 4px 16px rgb(0 0 0 / .08); }
.card img { display: block; width: 100%; aspect-ratio: 16 / 10; object-fit: cover; }
.card-body { padding: 16px; }
.card-body h3 { margin: 0 0 4px; }
.card-body p { margin: 0; color: #666; }
```
