# Express.js：ルート、パラメータ、クエリ

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

- `req.params`：パスの一部（`/users/42` → `{ id: '42' }`）、常に文字列。
- `req.query`：`?` 以降のパラメータ。これも文字列なので数値への変換は自分で行う。
- `req.body`：リクエスト本文。`express.json()` か `express.urlencoded()` を使った後だけ利用できる。
- ルートは宣言順に照合されるため、より具体的なパスを汎用的なパスより先に書く。
