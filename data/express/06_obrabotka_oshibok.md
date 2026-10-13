# Express.js: обработка ошибок

Обработчик ошибок — middleware с **четырьмя** аргументами, подключается последним:

```javascript
class HttpError extends Error {
  constructor(status, message) {
    super(message);
    this.status = status;
  }
}

app.get('/users/:id', async (req, res) => {
  const user = await db.findUser(req.params.id);
  if (!user) throw new HttpError(404, 'Пользователь не найден');
  res.json(user);
});

app.use((req, res) => {
  res.status(404).json({ error: 'Not Found' });
});

app.use((err, req, res, next) => {
  const status = err.status || 500;
  if (status >= 500) console.error(err);
  res.status(status).json({ error: status >= 500 ? 'Internal Server Error' : err.message });
});
```

В **Express 5** ошибки и отклонённые промисы из `async`-обработчиков автоматически попадают в обработчик ошибок. В Express 4 их нужно ловить вручную (`try/catch` + `next(err)`) или через пакет `express-async-errors`.

Не отдавайте клиенту стек и текст внутренних ошибок 500.
