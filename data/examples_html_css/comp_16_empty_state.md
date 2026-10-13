# Пример HTML/CSS: пустое состояние

Экран «ничего не найдено» с действием.

```html
<div class="empty"><div class="icon">📭</div><h3>No messages yet</h3><p>Start a conversation.</p><button>New message</button></div>
```

```css
.empty { display: grid; justify-items: center; gap: 8px; padding: 48px 16px; text-align: center; color: #555; }
.empty .icon { font-size: 48px; }
.empty h3 { margin: 0; color: #111; }
.empty p { margin: 0 0 8px; }
```
