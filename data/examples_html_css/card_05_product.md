# Пример HTML/CSS: карточка товара

Фото, название, цена, старая цена и кнопка «в корзину».

```html
<article class="product">
  <img src="sneakers.jpg" alt="White sneakers">
  <h3>Air Runner</h3>
  <p><strong>$89</strong> <s>$120</s></p>
  <button>Add to cart</button>
</article>
```

```css
.product { width: 220px; padding: 12px; border-radius: 14px; background: #fff; border: 1px solid #eee; }
.product img { width: 100%; aspect-ratio: 1; object-fit: cover; border-radius: 10px; background: #f5f5f7; }
.product h3 { font-size: 16px; margin: 10px 0 4px; }
.product s { color: #999; margin-left: 6px; }
.product button { width: 100%; margin-top: 8px; padding: 10px; border: 0; border-radius: 8px;
  background: #111; color: #fff; cursor: pointer; }
```
