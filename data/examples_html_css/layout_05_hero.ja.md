# HTML/CSS の例: 全画面ヒーロー

中央寄せテキストの全高ヒーローセクション。

```html
<section class="hero">
  <h1>Build faster</h1><p>Ship your next project in days, not months.</p><a href="#start">Start now</a>
</section>
```

```css
.hero { min-height: 100svh; display: grid; place-content: center; gap: 16px; padding: 24px;
  text-align: center; background: linear-gradient(160deg, #eef2ff, #fff); }
.hero h1 { margin: 0; font-size: clamp(2.5rem, 7vw, 5rem); line-height: 1.05; }
.hero p { margin: 0; color: #555; font-size: 1.25rem; }
.hero a { justify-self: center; padding: 14px 24px; border-radius: 12px; background: #4f46e5; color: #fff; text-decoration: none; }
```
