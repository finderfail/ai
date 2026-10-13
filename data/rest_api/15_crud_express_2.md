# REST API на Express: полный CRUD — часть 2

```javascript
app.post('/api/v1/users', (req, res) => {
  const { email, name } = req.body || {};
  if (typeof email !== 'string' || !email.includes('@')) {
    return problem(res, 400, 'Validation failed', 'Нужен корректный email');
  }
  const user = { id: crypto.randomUUID(), email, name: name || null, createdAt: new Date().toISOString() };
  users.set(user.id, user);
  res.status(201).location(`/api/v1/users/${user.id}`).json(user);
});

app.patch('/api/v1/users/:id', (req, res) => {
  const user = users.get(req.params.id);
  if (!user) return problem(res, 404, 'Not Found', 'Пользователь не найден');
  if (req.body.name !== undefined) user.name = req.body.name;
  res.json(user);
});

app.delete('/api/v1/users/:id', (req, res) => {
  if (!users.delete(req.params.id)) return problem(res, 404, 'Not Found', 'Пользователь не найден');
  res.sendStatus(204);
});

app.listen(3000);
```

В проекте `Map` заменяют БД, проверку — схемой zod.
