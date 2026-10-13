# HTML5: семантические элементы

```html
<header>
  <nav aria-label="Главное меню">
    <ul><li><a href="/">Главная</a></li><li><a href="/blog">Блог</a></li></ul>
  </nav>
</header>
<main>
  <article>
    <h1>Заголовок статьи</h1>
    <p>Текст…</p>
    <section>
      <h2>Раздел</h2>
      <figure>
        <img src="chart.png" alt="Рост продаж за год">
        <figcaption>Рис. 1. Продажи</figcaption>
      </figure>
    </section>
  </article>
  <aside>Похожие статьи</aside>
</main>
<footer><small>© 2026</small></footer>
```

- `<main>` — основное содержимое, один на странице.
- `<article>` — самостоятельный материал (пост, карточка товара).
- `<section>` — тематический раздел с заголовком.
- `<aside>` — дополнительное содержимое, `<nav>` — навигация.
- `<div>` и `<span>` — только для оформления, без смысла.

Семантика помогает скринридерам, поисковикам и упрощает CSS.
