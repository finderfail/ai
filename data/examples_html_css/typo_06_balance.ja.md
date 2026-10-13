# HTML/CSS の例: 見出しの改行をそろえる

text-wrap: balance と pretty できれいな行に。

```html
<h2 class="balanced">A heading that wraps across two lines nicely</h2>
```

```css
h1, h2, h3 { text-wrap: balance; }
p { text-wrap: pretty; }
.balanced { max-width: 22ch; }
```
