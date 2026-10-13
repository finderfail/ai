# Express.js：リクエストオブジェクト（req）

```javascript
app.post('/upload/:id', (req, res) => {
  req.params.id;
  req.query.sort;
  req.body;
  req.method;
  req.path;
  req.originalUrl;
  req.get('Authorization');
  req.headers['user-agent'];
  req.ip;
  req.protocol;
  req.hostname;
  req.cookies;
  req.is('application/json');
  req.accepts(['json', 'html']);
});
```

- リバースプロキシ（nginx、Caddy、Cloudflare）の背後では、`app.set('trust proxy', 1)` を設定するまで `req.ip`、`req.protocol`、`req.hostname` は正しくない。
- `req.cookies` は `cookie-parser` ミドルウェアがある場合のみ使える。
- Express 5 の `req.query` は読み取り専用のゲッターで、新しいオブジェクトを代入できない。検証結果は `req.validated` など別のフィールドに保存する。
- `req.body` は信用せず、必ずサーバー側で検証する。
