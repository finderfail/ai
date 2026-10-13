# HTML/CSS の例: 分割画面

画面を2分割：画像とフォーム。

```html
<div class="split"><div class="art"></div><div class="panel">Login form</div></div>
```

```css
.split { display: grid; grid-template-columns: 1fr 1fr; min-height: 100vh; }
.art { background: url(cover.jpg) center / cover; }
.panel { display: grid; place-items: center; padding: 32px; }
@media (max-width: 800px) { .split { grid-template-columns: 1fr; } .art { min-height: 200px; } }
```
