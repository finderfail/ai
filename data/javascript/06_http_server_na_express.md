# HTTP-сервер на Express

Express — внешняя зависимость, ставится через `npm install express`.

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

app.listen(3000, () => console.log('Express слушает порт 3000'));
```

Express сам разбирает маршруты и JSON-тело, но для простого сервиса встроенного модуля `http` достаточно.

Keywords: express, express server, middleware, javascript, node.js, js.
