# HTML/CSS の例: 「本文へスキップ」リンク

キーボードのフォーカスで現れる。

```html
<a class="skip" href="#main">Skip to content</a> … <main id="main">…</main>
```

```css
.skip { position: absolute; left: 8px; top: -48px; padding: 8px 14px; background: #111; color: #fff;
  border-radius: 8px; z-index: 100; transition: top .15s; }
.skip:focus { top: 8px; }
```
