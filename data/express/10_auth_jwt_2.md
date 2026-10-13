# Express.js: аутентификация по JWT — проверка и роли

```javascript
function auth(req, res, next) {
  const header = req.get('Authorization') || '';
  const token = header.startsWith('Bearer ') ? header.slice(7) : null;
  if (!token) return res.status(401).json({ error: 'Нет токена' });
  try {
    req.user = jwt.verify(token, SECRET);
    next();
  } catch {
    res.status(401).json({ error: 'Токен недействителен' });
  }
}

const allow = (...roles) => (req, res, next) =>
  roles.includes(req.user.role) ? next() : res.status(403).json({ error: 'Нет доступа' });

app.delete('/users/:id', auth, allow('admin'), removeUser);
```

401 — не аутентифицирован (нет токена или он неверный), 403 — аутентифицирован, но прав не хватает. Проверяйте права на каждый запрос, а не только при входе.
