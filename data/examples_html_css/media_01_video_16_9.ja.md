# HTML/CSS の例: レスポンシブ動画 16:9

比率を保つ埋め込み動画。

```html
<iframe class="video" src="https://www.youtube-nocookie.com/embed/ID" title="Demo" loading="lazy" allowfullscreen></iframe>
```

```css
.video { width: 100%; aspect-ratio: 16 / 9; border: 0; border-radius: 12px; }
```
