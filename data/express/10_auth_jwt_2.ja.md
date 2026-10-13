# Express.js：JWT による認証 — 検証とロール

```javascript
function auth(req, res, next) {
  const header = req.get('Authorization') || '';
  const token = header.startsWith('Bearer ') ? header.slice(7) : null;
  if (!token) return res.status(401).json({ error: 'トークンがありません' });
  try {
    req.user = jwt.verify(token, SECRET);
    next();
  } catch {
    res.status(401).json({ error: 'トークンが無効です' });
  }
}

const allow = (...roles) => (req, res, next) =>
  roles.includes(req.user.role) ? next() : res.status(403).json({ error: '権限がありません' });

app.delete('/users/:id', auth, allow('admin'), removeUser);
```

401 は未認証（トークンがないか無効）、403 は認証済みだが権限不足。ログイン時だけでなく、リクエストごとに権限を確認する。
