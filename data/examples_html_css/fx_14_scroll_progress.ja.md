# HTML/CSS の例: 読み進み具合のバー

JS なしのスクロール連動プログレス。

```html
<div class="read-progress"></div>
```

```css
.read-progress { position: fixed; top: 0; left: 0; height: 4px; width: 100%; background: #4f46e5;
  transform-origin: 0 50%; animation: grow linear; animation-timeline: scroll(root); }
@keyframes grow { from { transform: scaleX(0); } }
```
