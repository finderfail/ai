# Пример HTML/CSS: переключатель месяц/год

Переключение цен без JS через :has().

```html
<div class="pricing">
  <label><input type="checkbox" class="yearly"> Yearly</label>
  <p class="price"><span class="m">$12/mo</span><span class="y">$120/yr</span></p>
</div>
```

```css
.y { display: none; }
.pricing:has(.yearly:checked) .m { display: none; }
.pricing:has(.yearly:checked) .y { display: inline; }
.price { font-size: 32px; font-weight: 800; }
```
