# HTML/CSS の例: 料金ページ

3枚のカード、中央を強調。

```html
<section class="prices">
  <article><h3>Free</h3><p class="cost">$0</p><a href="#">Start</a></article>
  <article class="best"><h3>Pro</h3><p class="cost">$12</p><a href="#">Buy</a></article>
  <article><h3>Team</h3><p class="cost">$40</p><a href="#">Contact</a></article>
</section>
```

```css
.prices { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px; max-width: 900px; margin: auto; }
.prices article { padding: 28px; border: 1px solid #e5e7eb; border-radius: 18px; text-align: center; }
.prices .best { border: 2px solid #4f46e5; transform: scale(1.03); }
.cost { font-size: 40px; font-weight: 800; margin: 8px 0 20px; }
.prices a { display: block; padding: 10px; border-radius: 10px; background: #111; color: #fff; text-decoration: none; }
```
