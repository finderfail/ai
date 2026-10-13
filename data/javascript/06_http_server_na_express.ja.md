# Express による HTTP サーバー

Express は外部の依存パッケージで、`npm install express` で入れます。

```javascript
const express = require('express');
const os = require('os');

const app = express();
app.use(express.json());

app.get('/info', (req, res) => {
  res.json({
    platform: os.platform(),
    arch: os.arch(),
    cpuCount: os.cpus().length,
    totalMemoryMb: Math.round(os.totalmem() / 1024 / 1024)
  });
});

app.listen(3000, () => console.log('Express がポート 3000 で待機中'));
```

Express はルーティングや JSON 本文の解析を自動で行いますが、シンプルなサービスなら組み込みの `http` モジュールで十分です。

Keywords: express, express server, middleware, javascript, node.js, js.
