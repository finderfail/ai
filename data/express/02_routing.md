# Express.js: маршруты, параметры и query

```javascript
app.get('/users', (req, res) => {
  const { page = '1', limit = '20' } = req.query;
  res.json({ page: Number(page), limit: Number(limit) });
});

app.get('/users/:id', (req, res) => {
  res.json({ id: req.params.id });
});

app.post('/users', (req, res) => {
  res.status(201).json(req.body);
});

app.put('/users/:id', handler);
app.patch('/users/:id', handler);
app.delete('/users/:id', (req, res) => res.sendStatus(204));

app.route('/books')
  .get(listBooks)
  .post(createBook);
```

- `req.params` — части пути (`/users/42` → `{ id: '42' }`), всегда строки.
- `req.query` — параметры после `?`, тоже строки: приводите к числам сами.
- `req.body` — тело запроса, доступно только после `express.json()` или `express.urlencoded()`.
- Маршруты проверяются по порядку объявления: более конкретные пути ставьте раньше общих.
