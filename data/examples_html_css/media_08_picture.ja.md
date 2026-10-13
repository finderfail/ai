# HTML/CSS の例: 形式とテーマ対応の picture

ダークテーマや新しい形式向けに画像を切り替える。

```html
<picture>
  <source srcset="logo-dark.svg" media="(prefers-color-scheme: dark)">
  <source srcset="hero.avif" type="image/avif">
  <img src="hero.jpg" alt="Hero image" width="1200" height="600">
</picture>
```

```css
picture img { max-width: 100%; height: auto; display: block; }
```
