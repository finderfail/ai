# HTML/CSS の例: CSS だけのツールチップ

data 属性から hover とフォーカスで表示。

```html
<button class="tip" data-tip="Copy to clipboard">Copy</button>
```

```css
.tip { position: relative; }
.tip::after { content: attr(data-tip); position: absolute; bottom: calc(100% + 8px); left: 50%;
  transform: translateX(-50%); padding: 4px 8px; border-radius: 6px; background: #111; color: #fff;
  font-size: 12px; white-space: nowrap; opacity: 0; pointer-events: none; transition: opacity .15s; }
.tip:hover::after, .tip:focus-visible::after { opacity: 1; }
```
