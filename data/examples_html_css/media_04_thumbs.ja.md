# HTML/CSS の例: 同じサイズのサムネイル

比率の違う画像から正方形のサムネイル。

```html
<img class="thumb" src="any.jpg" alt="">
```

```css
.thumb { width: 120px; height: 120px; object-fit: cover; object-position: center; border-radius: 12px; }
```
