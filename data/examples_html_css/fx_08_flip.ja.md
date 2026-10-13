# HTML/CSS の例: 裏返るカード

hover で表と裏が3D回転。

```html
<div class="flip"><div class="flip-inner"><div class="front">Front</div><div class="back">Back</div></div></div>
```

```css
.flip { width: 240px; height: 160px; perspective: 800px; }
.flip-inner { position: relative; height: 100%; transition: transform .6s; transform-style: preserve-3d; }
.flip:hover .flip-inner { transform: rotateY(180deg); }
.front, .back { position: absolute; inset: 0; display: grid; place-items: center; border-radius: 14px; backface-visibility: hidden; }
.front { background: #eef2ff; } .back { background: #4f46e5; color: #fff; transform: rotateY(180deg); }
```
