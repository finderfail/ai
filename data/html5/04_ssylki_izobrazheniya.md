# HTML5: ссылки и изображения

```html
<a href="/about">О нас</a>
<a href="https://example.com" target="_blank" rel="noopener noreferrer">Внешняя ссылка</a>
<a href="mailto:info@example.com">Написать</a>
<a href="tel:+81312345678">Позвонить</a>
<a href="/file.pdf" download>Скачать PDF</a>
<a href="#contacts">К контактам</a>

<img src="photo.jpg" alt="Описание фото" width="800" height="600" loading="lazy" decoding="async">

<img src="small.jpg"
     srcset="small.jpg 480w, medium.jpg 960w, large.jpg 1600w"
     sizes="(max-width: 600px) 100vw, 50vw"
     alt="Пейзаж">

<picture>
  <source srcset="photo.avif" type="image/avif">
  <source srcset="photo.webp" type="image/webp">
  <img src="photo.jpg" alt="Пейзаж">
</picture>
```

- `alt` обязателен; для декоративных картинок — `alt=""`.
- `width`/`height` предотвращают «прыжки» страницы при загрузке.
- `loading="lazy"` откладывает загрузку картинок ниже экрана.
