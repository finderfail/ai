# 組み込みモジュール http による HTTP サーバー

`http` モジュールは Node.js の標準ライブラリに含まれており、インストールは不要です。

```javascript
const http = require('http');

const server = http.createServer((req, res) => {
  if (req.method === 'GET' && req.url === '/info') {
    res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
    res.end(JSON.stringify({ status: 'ok' }));
    return;
  }
  res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' });
  res.end('Not Found');
});

server.listen(3000, '127.0.0.1', () => {
  console.log('サーバー起動: http://127.0.0.1:3000');
});
```

要点：`createServer` はハンドラー `(req, res)` を受け取る。`req.method` と `req.url` でルートを判定。`res.writeHead(コード, ヘッダー)` でステータスを設定し、`res.end(本文)` で応答を終える。`res.end()` がないとリクエストは止まったままになります。

Keywords: http server, create server, listen port, request response, javascript, node.js, js.
