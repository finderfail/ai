# HTML/CSS の例: 自動で伸びる textarea

入力に合わせて伸びる入力欄（新しいブラウザ）。

```html
<textarea class="auto" rows="1" placeholder="Write a message…"></textarea>
```

```css
.auto { width: 100%; field-sizing: content; min-height: 44px; max-height: 240px;
  padding: 10px 14px; border: 1px solid #ccc; border-radius: 14px; resize: none; font: inherit; }
```
