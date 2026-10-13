# Пример HTML/CSS: карточка товара

Фото, название, цена и кнопка в корзину.

```html
<section class="product"><img src="shoe.jpg" alt="Running shoe">
<div><h1>Runner X</h1><p class="price">$129 <s>$159</s></p><p>Lightweight running shoe.</p><button>Add to cart</button></div></section>
```

```css
.product { display: grid; gap: 32px; max-width: 1000px; margin: auto; padding: 16px; }
@media (min-width: 800px) { .product { grid-template-columns: 1fr 1fr; align-items: center; } }
.product img { width: 100%; aspect-ratio: 1; object-fit: cover; border-radius: 20px; }
.price { font-size: 28px; font-weight: 800; } .price s { font-size: 18px; color: #9ca3af; font-weight: 400; }
.product button { padding: 14px 28px; border: 0; border-radius: 12px; background: #111; color: #fff; }
```
