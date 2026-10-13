# HTTP-сервер с эндпоинтом /info об операционной системе — часть 3

```javascript
  res.end(JSON.stringify({ error: 'Not Found' }));
});

server.listen(PORT, HOST, () => {
  console.log(`Сервер запущен: http://${HOST}:${PORT}/info`);
});
```

Данные берутся из модуля `os` в момент запроса, никаких файлов с заранее записанной информацией читать не нужно.

Keywords: http server endpoint, json api, system info endpoint, javascript, node.js, js.
