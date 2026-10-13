# HTML/CSS の例: hover で画像を拡大

枠の中でなめらかにズーム。

```html
<div class="zoom"><img src="photo.jpg" alt=""></div>
```

```css
.zoom { overflow: hidden; border-radius: 14px; }
.zoom img { display: block; width: 100%; transition: transform .4s ease; }
.zoom:hover img { transform: scale(1.08); }
```
