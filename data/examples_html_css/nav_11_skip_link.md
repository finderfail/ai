# Пример HTML/CSS: ссылка «к содержимому»

Скрытая ссылка для клавиатуры, видна при фокусе.

```html
<a href="#main" class="skip">Skip to content</a>
<main id="main">…</main>
```

```css
.skip { position: absolute; left: 8px; top: -60px; padding: 10px 14px; border-radius: 8px;
  background: #111; color: #fff; z-index: 100; transition: top .2s; }
.skip:focus { top: 8px; }
```
