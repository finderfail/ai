# HTML/CSS の例: サイトのヘッダー

左にロゴ、右にメニューとボタンを flexbox で配置。

```html
<header class="site-header">
  <a class="logo" href="/">Brand</a>
  <nav><a href="#features">Features</a><a href="#pricing">Pricing</a><a href="#faq">FAQ</a></nav>
  <a class="cta" href="#signup">Sign up</a>
</header>
```

```css
.site-header { display: flex; align-items: center; gap: 24px; padding: 16px 24px; border-bottom: 1px solid #eee; }
.logo { font-weight: 800; font-size: 20px; text-decoration: none; color: #111; }
.site-header nav { display: flex; gap: 20px; margin-left: auto; }
.site-header nav a { color: #444; text-decoration: none; }
.site-header nav a:hover { color: #4f46e5; }
.cta { padding: 8px 16px; border-radius: 8px; background: #4f46e5; color: #fff; text-decoration: none; }
```
