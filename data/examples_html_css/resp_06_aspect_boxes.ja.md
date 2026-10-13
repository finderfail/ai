# HTML/CSS の例: 比率固定のボックス

aspect-ratio で正方形、4:3、16:9。

```html
<div class="square"></div><div class="photo"></div><div class="wide"></div>
```

```css
.square { aspect-ratio: 1; } .photo { aspect-ratio: 4 / 3; } .wide { aspect-ratio: 16 / 9; }
.square, .photo, .wide { width: 100%; background: #e5e7eb; border-radius: 12px; }
```
