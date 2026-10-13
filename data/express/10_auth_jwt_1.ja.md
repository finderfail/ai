# Express.js：JWT による認証 — トークンの発行

```javascript
const jwt = require('jsonwebtoken');

const SECRET = process.env.JWT_SECRET;

app.post('/auth/login', async (req, res) => {
  const user = await checkPassword(req.body.email, req.body.password);
  if (!user) return res.status(401).json({ error: 'メールアドレスまたはパスワードが違います' });
  const token = jwt.sign({ sub: user.id, role: user.role }, SECRET, { expiresIn: '15m' });
  res.json({ accessToken: token });
});
```

- 秘密鍵は環境変数から読む長いランダム文字列にし、コードに書かない。
- アクセストークンの有効期限は短く（5〜15分）、延長にはリフレッシュトークンを使う。
- パスワードは bcrypt、argon2、scrypt でハッシュ化する。
- JWT に秘密情報を入れない。中身は鍵なしで読める。
- ブラウザ向けには、localStorage の JWT より `httpOnly` の cookie セッションのほうが安全。
