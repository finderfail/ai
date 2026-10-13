# HTML/CSS の例: カスタムチェックボックス

appearance: none で独自スタイルのチェックボックス。

```html
<label class="cb"><input type="checkbox"> I agree</label>
```

```css
.cb { display: inline-flex; align-items: center; gap: 8px; }
.cb input { appearance: none; width: 20px; height: 20px; border: 2px solid #9ca3af; border-radius: 6px;
  display: grid; place-content: center; cursor: pointer; }
.cb input::before { content: ""; width: 10px; height: 10px; transform: scale(0); transition: transform .12s;
  background: #fff; clip-path: polygon(14% 44%, 0 65%, 50% 100%, 100% 16%, 80% 0, 43% 62%); }
.cb input:checked { background: #4f46e5; border-color: #4f46e5; }
.cb input:checked::before { transform: scale(1); }
```
