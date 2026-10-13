# Express.js: структура проекта

Проверенная схема слоёв:

```
src/
  app.js            создание app, middleware, подключение роутеров
  server.js         app.listen, graceful shutdown
  config.js         чтение process.env
  routes/           маршруты: какие URL и какие middleware
  controllers/      разбор req, вызов сервиса, формирование res
  services/         бизнес-логика, не знает про Express
  repositories/     работа с БД
  middlewares/      auth, validate, errorHandler
  schemas/          схемы валидации
tests/
```

```javascript
exports.create = async (req, res) => {
  const user = await usersService.create(req.validated);
  res.status(201).location(`/api/v1/users/${user.id}`).json(user);
};
```

Разделение `app.js` (создаёт приложение) и `server.js` (запускает) позволяет тестировать приложение через supertest без запуска порта.

Сервисы не должны принимать `req`/`res` — так их легко переиспользовать и тестировать.
