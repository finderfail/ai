# HTML/CSS の例: 背景が交互のセクション

全幅の背景と狭い本文を持つ LP のセクション。

```html
<section class="band"><div class="inner">…</div></section>
<section class="band alt"><div class="inner">…</div></section>
```

```css
.band { padding: 80px 16px; }
.band.alt { background: #f8fafc; }
.inner { max-width: 960px; margin-inline: auto; }
```
