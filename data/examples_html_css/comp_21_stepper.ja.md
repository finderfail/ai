# HTML/CSS の例: 数量ステッパー

数値欄の両側に「−」と「+」ボタン。

```html
<div class="qty"><button aria-label="Decrease">−</button><input type="number" value="1" min="1" aria-label="Quantity"><button aria-label="Increase">+</button></div>
```

```css
.qty { display: inline-flex; border: 1px solid #d1d5db; border-radius: 10px; overflow: hidden; }
.qty button { width: 36px; border: 0; background: #f3f4f6; font-size: 18px; cursor: pointer; }
.qty input { width: 48px; border: 0; text-align: center; font: inherit; -moz-appearance: textfield; }
.qty input::-webkit-inner-spin-button { display: none; }
```
