# HTTP-сервер на встроенном модуле http

Модуль `http` входит в стандартную библиотеку Node.js, устанавливать ничего не нужно.

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
  console.log('Сервер слушает http://127.0.0.1:3000');
});
```

Ключевые моменты: `createServer` принимает обработчик `(req, res)`; `req.method` и `req.url` определяют маршрут; `res.writeHead(код, заголовки)` задаёт статус; `res.end(тело)` завершает ответ. Без `res.end()` запрос повиснет.

Keywords: http server, create server, listen port, request response, javascript, node.js, js.
