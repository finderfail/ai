# HTML/CSS の例: float を囲むコンテナ

clearfix の代わりに display: flow-root。

```html
<div class="media"><img class="left" src="a.jpg" alt="">Text…</div>
```

```css
.media { display: flow-root; }
.left { float: left; width: 120px; margin: 0 16px 8px 0; border-radius: 10px; }
```
