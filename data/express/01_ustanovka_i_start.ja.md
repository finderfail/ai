# Express.js：インストールと最初のサーバー

Express は Node.js 向けのミニマルな Web フレームワークで、ルーティング、ミドルウェア、使いやすい `req`/`res` を提供します。現在のメジャーバージョンは **Express 5**（2024年リリース、Node.js 18 以上が必要）。

```bash
mkdir api && cd api
npm init -y
npm install express
```

```javascript
const express = require('express');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

app.get('/health', (req, res) => {
  res.json({ status: 'ok' });
});

app.listen(PORT, () => {
  console.log(`サーバー: http://localhost:${PORT}`);
});
```

実行：`node server.js`。開発中は `node --watch server.js`（変更時に自動再起動、nodemon 不要）。

ESM を使う場合は package.json に `"type": "module"` を追加し、`import express from 'express'` と書きます。
