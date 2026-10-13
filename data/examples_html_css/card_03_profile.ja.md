# HTML/CSS の例: プロフィールカード

アバター、名前、役職、ボタンを中央に配置。

```html
<div class="profile">
  <img src="avatar.jpg" alt="" class="avatar">
  <h3>Anna Smith</h3><p>Frontend developer</p>
  <div class="actions"><button>Follow</button><button>Message</button></div>
</div>
```

```css
.profile { width: 260px; padding: 24px; text-align: center; border-radius: 20px; background: #fff;
  box-shadow: 0 6px 24px rgb(0 0 0 / .08); }
.avatar { width: 88px; height: 88px; border-radius: 50%; object-fit: cover; }
.profile h3 { margin: 12px 0 4px; } .profile p { margin: 0 0 16px; color: #777; }
.actions { display: flex; gap: 8px; justify-content: center; }
.actions button { padding: 8px 14px; border-radius: 8px; border: 1px solid #ddd; background: #fff; }
```
