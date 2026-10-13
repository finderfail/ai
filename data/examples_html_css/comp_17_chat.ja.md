# HTML/CSS の例: チャットの吹き出し

相手とユーザーのメッセージ。

```html
<div class="chat">
  <p class="msg in">Hi! How can I help?</p>
  <p class="msg out">I need a new invoice.</p>
</div>
```

```css
.chat { display: flex; flex-direction: column; gap: 8px; max-width: 480px; }
.msg { max-width: 75%; margin: 0; padding: 10px 14px; border-radius: 18px; line-height: 1.4; }
.msg.in { align-self: flex-start; background: #f1f2f5; border-bottom-left-radius: 4px; }
.msg.out { align-self: flex-end; background: #4f46e5; color: #fff; border-bottom-right-radius: 4px; }
```
