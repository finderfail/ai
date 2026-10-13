# Пример HTML/CSS: контейнер вокруг float

display: flow-root вместо clearfix.

```html
<div class="media"><img class="left" src="a.jpg" alt="">Text…</div>
```

```css
.media { display: flow-root; }
.left { float: left; width: 120px; margin: 0 16px 8px 0; border-radius: 10px; }
```
