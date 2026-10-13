# HTML/CSS の例: オンラインの点滅ドット

波紋付きのステータス表示。

```html
<span class="live">Live</span>
```

```css
.live { position: relative; padding-left: 18px; }
.live::before, .live::after { content: ""; position: absolute; left: 0; top: 50%; width: 10px; height: 10px;
  margin-top: -5px; border-radius: 50%; background: #22c55e; }
.live::after { animation: ping 1.5s ease-out infinite; }
@keyframes ping { to { transform: scale(2.5); opacity: 0; } }
```
