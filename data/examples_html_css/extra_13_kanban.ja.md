# HTML/CSS の例: カンバンボード

横スクロールする列とカード。

```html
<div class="board"><section><h3>To do</h3><article>Design</article></section>
<section><h3>Doing</h3><article>API</article></section><section><h3>Done</h3></section></div>
```

```css
.board { display: grid; grid-auto-flow: column; grid-auto-columns: minmax(260px, 1fr); gap: 16px; overflow-x: auto; padding: 8px; }
.board section { background: #f3f4f6; border-radius: 14px; padding: 12px; min-height: 300px; }
.board h3 { margin: 0 0 10px; font-size: 14px; color: #374151; }
.board article { background: #fff; padding: 12px; border-radius: 10px; box-shadow: 0 1px 3px rgb(0 0 0 / .08); margin-bottom: 8px; }
```
