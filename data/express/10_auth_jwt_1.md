# Express.js: аутентификация по JWT — выдача токена

```javascript
const jwt = require('jsonwebtoken');

const SECRET = process.env.JWT_SECRET;

app.post('/auth/login', async (req, res) => {
  const user = await checkPassword(req.body.email, req.body.password);
  if (!user) return res.status(401).json({ error: 'Неверный email или пароль' });
  const token = jwt.sign({ sub: user.id, role: user.role }, SECRET, { expiresIn: '15m' });
  res.json({ accessToken: token });
});
```

- Секрет — длинная случайная строка из переменной окружения, не из кода.
- Короткий срок жизни access-токена (5–15 минут) плюс refresh-токен для продления.
- Пароли хешируйте bcrypt, argon2 или scrypt.
- В JWT не кладите секреты: его содержимое читается без ключа.
- Для браузера надёжнее cookie-сессия с `httpOnly`, чем JWT в localStorage.
