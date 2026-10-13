# Пример HTML/CSS: фон-фото с затемнением

Фото на фоне с градиентным затемнением под текстом.

```html
<section class="banner"><h2>Explore Japan</h2></section>
```

```css
.banner { display: grid; align-items: end; min-height: 360px; padding: 32px; color: #fff; border-radius: 20px;
  background: linear-gradient(to top, rgb(0 0 0 / .7), transparent 60%), url(tokyo.jpg) center / cover; }
.banner h2 { margin: 0; font-size: 2rem; }
```
