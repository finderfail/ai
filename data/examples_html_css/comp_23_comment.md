# Пример HTML/CSS: комментарий

Аватар, имя, время и текст комментария.

```html
<article class="comment">
  <img src="u.jpg" alt="">
  <div><p class="meta"><b>Mika</b> · <time datetime="2026-10-12">2h ago</time></p><p>Great article, thanks!</p></div>
</article>
```

```css
.comment { display: flex; gap: 12px; padding: 12px 0; }
.comment img { width: 40px; height: 40px; border-radius: 50%; object-fit: cover; flex-shrink: 0; }
.comment p { margin: 0; } .meta { color: #777; font-size: 13px; margin-bottom: 4px !important; }
```
