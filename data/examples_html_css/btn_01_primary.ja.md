# HTML/CSS の例: プライマリボタン

塗りつぶし、hover、focus、押下の状態を持つボタン。

```html
<button class="btn">Get started</button>
```

```css
.btn {
  display: inline-flex; align-items: center; gap: 8px;
  padding: 12px 20px; border: 0; border-radius: 10px;
  background: #4f46e5; color: #fff; font: 600 16px/1 system-ui, sans-serif;
  cursor: pointer; transition: background .2s, transform .1s;
}
.btn:hover { background: #4338ca; }
.btn:active { transform: scale(.97); }
.btn:focus-visible { outline: 3px solid #a5b4fc; outline-offset: 2px; }
```
