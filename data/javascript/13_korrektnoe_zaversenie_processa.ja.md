# プロセスの正しい終了

```javascript
const server = http.createServer(handler);
server.listen(3000);

process.on('SIGINT', () => {
  console.log('停止しています...');
  server.close(() => process.exit(0));
});
```

`server.close()` は新しい接続の受け付けをやめ、処理中の接続が終わるのを待ちます。

Keywords: graceful shutdown, sigint, close server, javascript, node.js, js.
