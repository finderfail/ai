# Express.js：組み込みミドルウェア

```javascript
app.use(express.json({ limit: '1mb' }));
app.use(express.urlencoded({ extended: false }));
app.use(express.static('public', { maxAge: '1d' }));
app.use(express.text());
app.use(express.raw({ type: 'application/octet-stream' }));
```

- **express.json()**：`Content-Type: application/json` の本文を `req.body` に解析。`limit` で大きすぎる本文を防ぐ（既定は100kb）。
- **express.urlencoded()**：`application/x-www-form-urlencoded` のフォーム。Express 5 では既定で `extended: false`。
- **express.static()**：フォルダのファイルを配信。ルートより前か、専用のプレフィックスで登録：`app.use('/assets', express.static('public'))`。
- **express.raw()**：Webhook の署名検証（Stripe など）のように、本文の元のバイト列が必要な場合に使う。

`req.body` が `undefined` なら、パーサーの登録忘れか、クライアントが正しい Content-Type を送っていない。
