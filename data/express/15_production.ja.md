# Express.js：本番環境での運用

```javascript
const server = app.listen(PORT);

function shutdown(signal) {
  console.log(`${signal}: 停止します`);
  server.close(() => process.exit(0));
  setTimeout(() => process.exit(1), 10_000).unref();
}

process.on('SIGTERM', shutdown);
process.on('SIGINT', shutdown);
```

チェックリスト：
- `NODE_ENV=production`：テンプレートのキャッシュを有効にし、エラーを簡潔にする。
- nginx/Caddy/ロードバランサーの背後なら `app.set('trust proxy', 1)`。
- TLS はリバースプロキシで終端し、Express は localhost で待ち受ける。
- ログは stdout に JSON で（pino）。ホットパスで console.log を使わない。
- プロセス管理：systemd、Docker（`restart: unless-stopped`）、PM2。
- ロードバランサー用のヘルスチェック `/health`。
- 圧縮（`compression`）を有効にするか、プロキシに任せる。
- 設定は環境変数だけで行う（Node 20.6 以降は `node --env-file=.env`）。
