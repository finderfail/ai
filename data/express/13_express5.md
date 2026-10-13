# Express.js: что изменилось в Express 5

- Требуется **Node.js 18+**.
- **Async-ошибки**: отклонённые промисы и `throw` в `async`-обработчиках автоматически уходят в обработчик ошибок.
- **Новый синтаксис путей** (path-to-regexp 8):
  - звёздочка должна быть именованной: `/files/*splat` вместо `/files/*`;
  - необязательная часть — в фигурных скобках: `/users{/:id}` вместо `/users/:id?`;
  - регулярные выражения внутри строк путей больше не поддерживаются.
- `req.query` только для чтения; парсер query по умолчанию «simple».
- `express.urlencoded()` по умолчанию `extended: false`.
- Удалены устаревшие методы: `app.del` → `app.delete`, `res.sendfile` → `res.sendFile`, `req.param()` → `req.params` / `req.query` / `req.body`, `res.send(status, body)` → `res.status(status).send(body)`.
- `res.redirect('back')` удалён: `req.get('Referrer') || '/'`.
- `res.status()` принимает только целые числа 100–999.

Миграция: `npm install express@5`, исправить пути со `*` и `?`, прогнать тесты.
