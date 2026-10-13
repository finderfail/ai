# Пример HTML/CSS: цитата

Цитата с большой кавычкой и подписью.

```html
<figure class="pull"><blockquote>Simplicity is prerequisite for reliability.</blockquote><figcaption>— E. Dijkstra</figcaption></figure>
```

```css
.pull { margin: 2em 0; padding-left: 20px; border-left: 4px solid #4f46e5; }
.pull blockquote { margin: 0; font-size: 1.4em; font-style: italic; line-height: 1.4; }
.pull blockquote::before { content: "\201C"; font-size: 2em; line-height: 0; vertical-align: -.4em; color: #4f46e5; }
.pull figcaption { margin-top: 8px; color: #666; }
```
