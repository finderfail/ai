# HTML5: доступность (a11y) и ARIA

Основные правила:
- Используйте **правильные элементы**: кнопка — `<button>`, ссылка — `<a href>`, а не `<div onclick>`.
- У изображений — `alt`, у полей — `<label>`, у страницы — `lang`.
- Заголовки по порядку, один `<h1>`.
- Всё доступно с клавиатуры; фокус видим (`:focus-visible`).
- Контраст текста не ниже 4.5:1.

ARIA — только когда нет подходящего HTML-элемента:
```html
<button aria-expanded="false" aria-controls="menu">Меню</button>
<ul id="menu" hidden>…</ul>

<button aria-label="Закрыть">×</button>
<div role="alert">Ошибка сохранения</div>
<div aria-live="polite">Загружено 3 файла</div>
<span class="visually-hidden">Текст только для скринридеров</span>
<nav aria-label="Хлебные крошки">…</nav>
<a href="#main" class="skip-link">Перейти к содержимому</a>
```

Первое правило ARIA: не используйте ARIA, если можно обойтись нативным элементом.
