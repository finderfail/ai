# フレームワークなしで複数のエンドポイントをルーティング

```javascript
const routes = {
  'GET /info': (req, res) => sendJson(res, 200, getSystemInfo()),
  'GET /health': (req, res) => sendJson(res, 200, { status: 'ok' })
};

function sendJson(res, code, data) {
  res.writeHead(code, { 'Content-Type': 'application/json; charset=utf-8' });
  res.end(JSON.stringify(data));
}

const server = http.createServer((req, res) => {
  const url = new URL(req.url, `http://${req.headers.host}`);
  const handler = routes[`${req.method} ${url.pathname}`];
  if (handler) {
    handler(req, res);
  } else {
    sendJson(res, 404, { error: 'Not Found' });
  }
});
```

`new URL(req.url, base)` でパスとクエリパラメータを分けられます：`url.pathname` は `/info`、`url.searchParams.get('key')` はパラメータの値です。

Keywords: routing, routes, url path, query params, javascript, node.js, js.
