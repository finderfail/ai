# HTML/CSS の例: 固定ヘッダーの表

ボックス内でスクロールし見出しは上に残る。

```html
<div class="table-wrap"><table>…</table></div>
```

```css
.table-wrap { max-height: 360px; overflow: auto; border: 1px solid #e5e7eb; border-radius: 10px; }
.table-wrap table { width: 100%; border-collapse: collapse; }
.table-wrap thead th { position: sticky; top: 0; background: #fff; box-shadow: 0 1px 0 #e5e7eb; }
.table-wrap td, .table-wrap th { padding: 8px 12px; }
```
