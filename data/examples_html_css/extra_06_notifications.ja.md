# HTML/CSS の例: 通知リスト

未読はドットで強調。

```html
<ul class="notes"><li class="unread"><b>New comment</b><time>2m</time></li><li><b>Payment received</b><time>1h</time></li></ul>
```

```css
.notes { list-style: none; padding: 0; max-width: 420px; }
.notes li { display: flex; justify-content: space-between; gap: 12px; padding: 12px 16px; border-radius: 10px; }
.notes li:hover { background: #f3f4f6; }
.notes time { color: #9ca3af; font-size: 13px; }
.unread b::before { content: ""; display: inline-block; width: 8px; height: 8px; margin-right: 8px; border-radius: 50%; background: #4f46e5; }
```
