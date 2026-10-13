# HTML/CSS の例: チャット画面

メッセージ一覧と下部の入力欄。

```html
<div class="chat"><div class="msgs"><p class="msg in">Hi!</p><p class="msg out">Hello 👋</p></div>
<form class="composer"><input placeholder="Message"><button>Send</button></form></div>
```

```css
.chat { display: flex; flex-direction: column; height: 100dvh; }
.msgs { flex: 1; overflow-y: auto; display: flex; flex-direction: column; gap: 8px; padding: 16px; }
.msg { max-width: 75%; margin: 0; padding: 10px 14px; border-radius: 16px; }
.in { align-self: flex-start; background: #f1f1f4; }
.out { align-self: flex-end; background: #4f46e5; color: #fff; }
.composer { display: flex; gap: 8px; padding: 12px; border-top: 1px solid #eee; }
.composer input { flex: 1; padding: 10px 14px; border: 1px solid #ddd; border-radius: 999px; }
```
