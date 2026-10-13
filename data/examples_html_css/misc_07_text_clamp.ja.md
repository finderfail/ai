# HTML/CSS の例: テキストの省略記号

1行と複数行の省略。

```html
<p class="one">Very long title…</p><p class="three">Long description…</p>
```

```css
.one { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.three { display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }
```
