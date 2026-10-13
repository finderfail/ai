# REST API на Express: полный CRUD — часть 1

```javascript
const express = require('express');
const crypto = require('node:crypto');

const app = express();
app.use(express.json());

const users = new Map();

function problem(res, status, title, detail) {
  res.status(status).type('application/problem+json').json({ type: 'about:blank', title, status, detail });
}

app.get('/api/v1/users', (req, res) => {
  const limit = Math.min(Number(req.query.limit) || 20, 100);
  const offset = Number(req.query.offset) || 0;
  const all = [...users.values()];
  res.json({ data: all.slice(offset, offset + limit), meta: { total: all.length, limit, offset } });
});

app.get('/api/v1/users/:id', (req, res) => {
  const user = users.get(req.params.id);
  if (!user) return problem(res, 404, 'Not Found', 'Пользователь не найден');
  res.json(user);
});
```

Продолжение (создание, изменение, удаление) — во второй части.
