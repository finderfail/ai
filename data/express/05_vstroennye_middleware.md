# Express.js: встроенные middleware

```javascript
app.use(express.json({ limit: '1mb' }));
app.use(express.urlencoded({ extended: false }));
app.use(express.static('public', { maxAge: '1d' }));
app.use(express.text());
app.use(express.raw({ type: 'application/octet-stream' }));
```

- **express.json()** — разбирает тело с `Content-Type: application/json` в `req.body`. Опция `limit` защищает от слишком больших тел (по умолчанию 100kb).
- **express.urlencoded()** — формы `application/x-www-form-urlencoded`. В Express 5 по умолчанию `extended: false`.
- **express.static()** — раздаёт файлы из папки. Подключайте до маршрутов или на отдельном префиксе: `app.use('/assets', express.static('public'))`.
- **express.raw()** нужен, например, для проверки подписи вебхуков (Stripe и др.), где важны исходные байты тела.

Если `req.body` равен `undefined` — вы забыли подключить парсер или клиент не прислал правильный Content-Type.
