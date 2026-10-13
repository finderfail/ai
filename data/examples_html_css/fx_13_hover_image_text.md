# Пример HTML/CSS: текст поверх картинки при наведении

Подпись выезжает снизу на карточке-изображении.

```html
<figure class="reveal-card"><img src="p.jpg" alt=""><figcaption>Project Alpha</figcaption></figure>
```

```css
.reveal-card { position: relative; overflow: hidden; margin: 0; border-radius: 14px; }
.reveal-card img { display: block; width: 100%; }
.reveal-card figcaption { position: absolute; inset: auto 0 0; padding: 16px; color: #fff;
  background: linear-gradient(transparent, rgb(0 0 0 / .7)); transform: translateY(100%); transition: transform .3s; }
.reveal-card:hover figcaption, .reveal-card:focus-within figcaption { transform: none; }
```
