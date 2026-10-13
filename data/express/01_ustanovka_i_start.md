# Express.js: установка и первый сервер

Express — минималистичный веб-фреймворк для Node.js: маршрутизация, middleware, удобные `req`/`res`. Актуальная мажорная версия — **Express 5** (вышла в 2024 году, требует Node.js 18+).

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
  console.log(`Сервер: http://localhost:${PORT}`);
});
```

Запуск: `node server.js`, во время разработки — `node --watch server.js` (перезапуск при изменениях, без nodemon).

Для ESM добавьте `"type": "module"` в package.json и пишите `import express from 'express'`.
