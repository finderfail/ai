# Express.js: middleware

Middleware — функция `(req, res, next)`, которая выполняется между получением запроса и отправкой ответа. Она может изменить `req`/`res`, завершить ответ или передать управление дальше через `next()`.

```javascript
function requestTime(req, res, next) {
  req.startedAt = Date.now();
  next();
}

function requireJson(req, res, next) {
  if (req.method !== 'GET' && !req.is('application/json')) {
    return res.status(415).json({ error: 'Нужен Content-Type: application/json' });
  }
  next();
}

app.use(requestTime);
app.use('/api', requireJson);
app.get('/admin', checkAdmin, adminHandler);
```

Правила:
- Порядок `app.use` важен: middleware выполняются в порядке подключения.
- Каждая middleware должна либо вызвать `next()`, либо отправить ответ — иначе запрос «зависнет».
- `next(err)` с аргументом сразу передаёт управление обработчику ошибок.
- Не вызывайте `next()` после отправки ответа — получите ошибку «Cannot set headers after they are sent».
