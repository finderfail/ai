# OS 情報を返す /info エンドポイント付き HTTP サーバー — その3

```javascript
  res.end(JSON.stringify({ error: 'Not Found' }));
});

server.listen(PORT, HOST, () => {
  console.log(`サーバー起動: http://${HOST}:${PORT}/info`);
});
```

データはリクエストの時点で `os` モジュールから取得されます。あらかじめ情報を書いたファイルを読む必要はありません。

Keywords: http server endpoint, json api, system info endpoint, javascript, node.js, js.
