# HTML/CSS の例: ランディングページ

ヘッダー・ヒーロー・特長の1ページ。

```html
<header class="top"><b>Brand</b><a href="#start">Start</a></header>
<section class="hero"><h1>Build faster</h1><p>One tool for your whole team.</p><a id="start" href="/signup">Try free</a></section>
<section class="feats"><div>Fast</div><div>Secure</div><div>Simple</div></section>
```

```css
.top { display: flex; justify-content: space-between; padding: 16px 24px; }
.hero { text-align: center; padding: 80px 16px; }
.hero h1 { font-size: clamp(2.5rem, 6vw, 4rem); margin: 0 0 12px; }
.hero a { display: inline-block; margin-top: 16px; padding: 12px 24px; background: #4f46e5; color: #fff; border-radius: 12px; text-decoration: none; }
.feats { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; max-width: 960px; margin: auto; padding: 16px; }
.feats div { padding: 24px; border-radius: 16px; background: #f5f6f8; }
```
