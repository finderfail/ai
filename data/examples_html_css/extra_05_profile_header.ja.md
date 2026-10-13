# HTML/CSS の例: プロフィールヘッダー

カバー画像、重なるアバター、名前。

```html
<header class="profile"><div class="cover"></div><img class="ava" src="me.jpg" alt="">
<h1>Ann Lee</h1><p>Frontend developer</p></header>
```

```css
.profile { text-align: center; }
.cover { height: 180px; border-radius: 16px; background: linear-gradient(120deg, #6366f1, #ec4899); }
.ava { width: 112px; height: 112px; margin-top: -56px; border-radius: 50%; border: 4px solid #fff; object-fit: cover; }
.profile h1 { margin: 8px 0 0; font-size: 24px; }
.profile p { margin: 4px 0; color: #6b7280; }
```
