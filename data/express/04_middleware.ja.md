# Express.js：ミドルウェア

ミドルウェアは、リクエストを受けてからレスポンスを返すまでの間に実行される関数 `(req, res, next)` です。`req`/`res` を変更したり、レスポンスを終えたり、`next()` で次に処理を渡したりできます。

```javascript
function requestTime(req, res, next) {
  req.startedAt = Date.now();
  next();
}

function requireJson(req, res, next) {
  if (req.method !== 'GET' && !req.is('application/json')) {
    return res.status(415).json({ error: 'Content-Type: application/json が必要です' });
  }
  next();
}

app.use(requestTime);
app.use('/api', requireJson);
app.get('/admin', checkAdmin, adminHandler);
```

ルール：
- `app.use` の順序が重要で、登録した順に実行される。
- 各ミドルウェアは `next()` を呼ぶかレスポンスを返す。どちらもしないとリクエストが「止まる」。
- 引数付きの `next(err)` はすぐにエラーハンドラーへ処理を渡す。
- レスポンス送信後に `next()` を呼ばない。「Cannot set headers after they are sent」エラーになる。
