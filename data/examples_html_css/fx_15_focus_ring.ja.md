# HTML/CSS の例: フォーカスリング

キーボード操作時だけ見えるフォーカス。

```html
<button>Save</button><a href="#">Link</a>
```

```css
:focus { outline: none; }
:focus-visible { outline: 3px solid #a5b4fc; outline-offset: 2px; border-radius: 6px; }
```
