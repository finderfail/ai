# HTML/CSS の例: カンバンボード

横スクロールするタスクの列。

```html
<div class="board">
  <section class="column"><h3>To do</h3><div class="task">Write docs</div></section>
  <section class="column"><h3>Doing</h3><div class="task">API</div></section>
</div>
```

```css
.board { display: flex; gap: 16px; overflow-x: auto; padding: 16px; scroll-snap-type: x mandatory; }
.column { flex: 0 0 280px; padding: 12px; border-radius: 14px; background: #f1f2f5; scroll-snap-align: start; }
.task { padding: 12px; margin-top: 8px; border-radius: 10px; background: #fff; box-shadow: 0 1px 3px rgb(0 0 0 / .08); }
```
