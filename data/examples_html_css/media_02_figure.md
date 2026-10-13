# Пример HTML/CSS: изображение с подписью

figure и figcaption с оформлением.

```html
<figure class="fig"><img src="chart.png" alt="Sales growth chart"><figcaption>Fig. 1 — Sales growth</figcaption></figure>
```

```css
.fig { margin: 24px 0; }
.fig img { display: block; width: 100%; height: auto; border-radius: 12px; }
.fig figcaption { margin-top: 8px; font-size: 14px; color: #666; text-align: center; }
```
