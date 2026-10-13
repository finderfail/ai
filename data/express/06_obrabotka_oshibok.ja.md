# Express.js：エラー処理

エラーハンドラーは **4つ** の引数を持つミドルウェアで、最後に登録します：

```javascript
class HttpError extends Error {
  constructor(status, message) {
    super(message);
    this.status = status;
  }
}

app.get('/users/:id', async (req, res) => {
  const user = await db.findUser(req.params.id);
  if (!user) throw new HttpError(404, 'ユーザーが見つかりません');
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

**Express 5** では、`async` ハンドラーのエラーや拒否された Promise が自動でエラーハンドラーに渡る。Express 4 では手動で捕捉する（`try/catch` + `next(err)`）か、`express-async-errors` パッケージを使う。

500 エラーのスタックや内部のメッセージをクライアントに返さないこと。
