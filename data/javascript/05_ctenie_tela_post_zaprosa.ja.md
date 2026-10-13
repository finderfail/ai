# POST リクエストの本文を読む

本文はストリームで届くので、手動で組み立てる必要があります。

```javascript
function readBody(req) {
  return new Promise((resolve, reject) => {
    const chunks = [];
    req.on('data', (chunk) => chunks.push(chunk));
    req.on('end', () => resolve(Buffer.concat(chunks).toString('utf8')));
    req.on('error', reject);
  });
}

const server = http.createServer(async (req, res) => {
  if (req.method === 'POST' && req.url === '/echo') {
    const raw = await readBody(req);
    const data = JSON.parse(raw);
    sendJson(res, 200, data);
  }
});
```

Keywords: read request body, post body, parse json body, javascript, node.js, js.
