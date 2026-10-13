# HTML5: структура документа

```html
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Название страницы</title>
  <meta name="description" content="Краткое описание для поисковиков">
  <link rel="icon" href="/favicon.ico">
  <link rel="stylesheet" href="/styles.css">
  <script src="/app.js" defer></script>
</head>
<body>
  <h1>Заголовок</h1>
</body>
</html>
```

- `<!DOCTYPE html>` — короткий доктайп HTML5, включает стандартный режим браузера.
- `lang` на `<html>` нужен для озвучки, переводчиков и SEO.
- `<meta charset="utf-8">` — первым в `<head>`.
- `defer` — скрипт загружается параллельно и выполняется после разбора HTML; `async` — сразу по загрузке, без порядка.
- HTML сейчас развивается как «живой стандарт» WHATWG (HTML Living Standard).
