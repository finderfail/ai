# HTML/CSS の例: scroll-snap のカルーセル

JS なしでスワイプしスナップするスライド。

```html
<div class="carousel"><img src="1.jpg" alt=""><img src="2.jpg" alt=""><img src="3.jpg" alt=""></div>
```

```css
.carousel { display: flex; gap: 12px; overflow-x: auto; scroll-snap-type: x mandatory; scrollbar-width: none; }
.carousel > * { flex: 0 0 85%; scroll-snap-align: center; border-radius: 14px; }
@media (min-width: 768px) { .carousel > * { flex-basis: 40%; } }
```
