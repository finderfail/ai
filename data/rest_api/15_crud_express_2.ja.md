# Express による REST API：完全な CRUD — その2

```javascript
app.post('/api/v1/users', (req, res) => {
  const { email, name } = req.body || {};
  if (typeof email !== 'string' || !email.includes('@')) {
    return problem(res, 400, 'Validation failed', '正しいメールアドレスが必要です');
  }
  const user = { id: crypto.randomUUID(), email, name: name || null, createdAt: new Date().toISOString() };
  users.set(user.id, user);
  res.status(201).location(`/api/v1/users/${user.id}`).json(user);
});

app.patch('/api/v1/users/:id', (req, res) => {
  const user = users.get(req.params.id);
  if (!user) return problem(res, 404, 'Not Found', 'ユーザーが見つかりません');
  if (req.body.name !== undefined) user.name = req.body.name;
  res.json(user);
});

app.delete('/api/v1/users/:id', (req, res) => {
  if (!users.delete(req.params.id)) return problem(res, 404, 'Not Found', 'ユーザーが見つかりません');
  res.sendStatus(204);
});

app.listen(3000);
```

実際のプロジェクトでは `Map` をデータベースに、検証をスキーマ（zod）に置き換える。
