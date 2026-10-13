# CORS и заголовки ответа

```javascript
function applyCors(res, origin = '*') {
  res.setHeader('Access-Control-Allow-Origin', origin);
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
}

const server = http.createServer((req, res) => {
  applyCors(res);

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  res.setHeader('Cache-Control', 'no-store');
  res.writeHead(200, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({ ok: true }));
});
```

Браузер шлёт предварительный OPTIONS-запрос перед POST с нестандартными заголовками — на него нужно ответить кодом 204.

Keywords: cors, headers, options preflight, javascript, node.js, js.
