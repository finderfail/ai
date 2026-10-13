# HTML/CSS の例: 空の状態

データがないときの表示。

```html
<div class="empty"><div class="icon">📭</div><h3>No messages yet</h3><p>Start a new chat.</p><button>New chat</button></div>
```

```css
.empty { display: grid; justify-items: center; gap: 6px; padding: 48px 16px; text-align: center; color: #6b7280; }
.empty .icon { font-size: 48px; }
.empty h3 { margin: 0; color: #111; }
.empty button { margin-top: 10px; padding: 10px 18px; border: 0; border-radius: 10px; background: #4f46e5; color: #fff; }
```
