# Пример HTML/CSS: страница статьи блога

Удобная для чтения колонка текста.

```html
<article class="post"><h1>Why CSS Grid</h1><p class="by">Oct 12, 2026 · 6 min</p>
<p>Lead paragraph…</p><h2>Basics</h2><p>…</p><pre><code>display: grid;</code></pre></article>
```

```css
.post { max-width: 68ch; margin: 48px auto; padding: 0 16px; font-size: 18px; line-height: 1.7; }
.post h1 { font-size: 2.4rem; line-height: 1.15; margin-bottom: 4px; }
.by { color: #6b7280; font-size: 14px; }
.post pre { background: #0f172a; color: #e2e8f0; padding: 16px; border-radius: 10px; overflow-x: auto; }
.post img { max-width: 100%; border-radius: 12px; }
```
