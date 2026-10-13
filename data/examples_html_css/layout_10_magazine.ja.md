# HTML/CSS の例: 雑誌風レイアウト

grid-template-areas でメイン記事とニュース欄。

```html
<section class="mag">
  <article class="lead">Lead story</article><article class="s1">Story</article>
  <article class="s2">Story</article><aside class="news">Latest</aside>
</section>
```

```css
.mag { display: grid; gap: 16px; grid-template-columns: 2fr 1fr 1fr;
  grid-template-areas: "lead lead news" "s1 s2 news"; }
.lead { grid-area: lead; min-height: 300px; } .s1 { grid-area: s1; } .s2 { grid-area: s2; } .news { grid-area: news; }
.mag > * { padding: 16px; border-radius: 12px; background: #f5f5f7; }
@media (max-width: 800px) { .mag { grid-template-columns: 1fr; grid-template-areas: "lead" "s1" "s2" "news"; } }
```
