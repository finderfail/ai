# HTML/CSS の例: カレンダーのグリッド

7列の日付グリッド。

```html
<div class="cal"><b>Mo</b><b>Tu</b><b>We</b><b>Th</b><b>Fr</b><b>Sa</b><b>Su</b>
<span class="start">1</span><span>2</span><span class="today">3</span><span>4</span></div>
```

```css
.cal { display: grid; grid-template-columns: repeat(7, 1fr); gap: 4px; max-width: 320px; text-align: center; }
.cal b { font-size: 12px; color: #6b7280; padding: 4px 0; }
.cal span { aspect-ratio: 1; display: grid; place-items: center; border-radius: 8px; }
.cal span:hover { background: #f3f4f6; }
.cal .start { grid-column-start: 3; }
.cal .today { background: #4f46e5; color: #fff; }
```
