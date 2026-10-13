# HTML/CSS の例: 区切り付きの横並びリスト

点で区切った横並びの項目。

```html
<ul class="meta"><li>Oct 12</li><li>5 min read</li><li>CSS</li></ul>
```

```css
.meta { display: flex; flex-wrap: wrap; list-style: none; padding: 0; color: #6b7280; font-size: 14px; }
.meta li + li::before { content: "·"; margin: 0 8px; }
```
