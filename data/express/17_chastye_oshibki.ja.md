# Express.js：よくあるミス

- **`req.body` が undefined**：`express.json()` が未登録か、クライアントが `Content-Type: application/json` を送っていない。
- **Cannot set headers after they are sent**：レスポンスを2回送っている。`res.json()` の後に `return` がない、またはレスポンス後に `next()` を呼んでいる。
- **リクエストが止まる**：ミドルウェアが `next()` も応答もしていない。
- **存在するはずのルートで 404**：パスの誤字、メソッドの違い、ルーターのプレフィックスの違い。
- **エラーハンドラーが動かない**：引数が4つでないか、ルートより前に登録されている。
- **ブラウザで CORS エラー**：そのドメイン向けの `Access-Control-Allow-Origin` を返していないか、プリフライトの OPTIONS に応答していない。
- **プロキシの背後で req.ip が違う**：`trust proxy` が無効。
- **Express 4 で落ちた Promise**：async のエラーが `next(err)` に渡されていない。Express 5 では解消。
- **5 に更新後のパス構文エラー**：`*` と `?` を含むパスを新しい構文に書き換える。
- **EADDRINUSE**：ポート使用中。`lsof -i :3000` でプロセスを探す。
