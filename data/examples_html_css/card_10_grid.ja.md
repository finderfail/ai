# HTML/CSS の例: カードのグリッド

高さがそろうレスポンシブなカードグリッド。

```html
<section class="cards">
  <article class="card"><h3>One</h3><p>Short text.</p></article>
  <article class="card"><h3>Two</h3><p>A bit longer text for this card.</p></article>
  <article class="card"><h3>Three</h3><p>Text.</p></article>
</section>
```

```css
.cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 16px; }
.card { display: flex; flex-direction: column; padding: 20px; border-radius: 14px;
  background: #fff; border: 1px solid #e5e7eb; }
.card p { flex: 1; color: #555; }
```
