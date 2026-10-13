# Корректное завершение процесса

```javascript
const server = http.createServer(handler);
server.listen(3000);

process.on('SIGINT', () => {
  console.log('Останавливаюсь...');
  server.close(() => process.exit(0));
});
```

`server.close()` перестаёт принимать новые соединения и ждёт завершения текущих.

Keywords: graceful shutdown, sigint, close server, javascript, node.js, js.
