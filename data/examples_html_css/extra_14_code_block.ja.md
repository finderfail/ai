# HTML/CSS の例: コピーボタン付きコードブロック

暗いコードブロックと角のボタン。

```html
<div class="code"><button onclick="navigator.clipboard.writeText(this.nextElementSibling.innerText)">Copy</button>
<pre><code>npm install express</code></pre></div>
```

```css
.code { position: relative; }
.code pre { margin: 0; padding: 16px; border-radius: 12px; background: #0f172a; color: #e2e8f0; overflow-x: auto;
  font: 14px/1.5 ui-monospace, Menlo, monospace; }
.code button { position: absolute; top: 8px; right: 8px; padding: 4px 10px; border: 0; border-radius: 6px;
  background: #334155; color: #e2e8f0; font-size: 12px; cursor: pointer; }
```
