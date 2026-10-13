# Express.js：プロジェクト構成

実績のあるレイヤー構成：

```
src/
  app.js            app の作成、ミドルウェア、ルーターの接続
  server.js         app.listen、グレースフルシャットダウン
  config.js         process.env の読み込み
  routes/           ルート：どの URL にどのミドルウェアか
  controllers/      req の解析、サービス呼び出し、res の作成
  services/         ビジネスロジック、Express を知らない
  repositories/     データベース操作
  middlewares/      auth、validate、errorHandler
  schemas/          検証スキーマ
tests/
```

```javascript
exports.create = async (req, res) => {
  const user = await usersService.create(req.validated);
  res.status(201).location(`/api/v1/users/${user.id}`).json(user);
};
```

`app.js`（アプリを作る）と `server.js`（起動する）を分けると、ポートを開かずに supertest でアプリをテストできる。

サービスは `req`/`res` を受け取らないようにすると、再利用やテストが簡単になる。
