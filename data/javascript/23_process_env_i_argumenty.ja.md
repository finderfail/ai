# 環境変数とプロセスの終了

```javascript
const port = Number(process.env.PORT) || 3000;
const isProduction = process.env.NODE_ENV === 'production';

if (!process.env.API_KEY) {
  console.error('変数 API_KEY が設定されていません');
  process.exit(1);
}

process.on('uncaughtException', (error) => {
  console.error('未処理のエラー:', error);
  process.exit(1);
});

process.on('unhandledRejection', (reason) => {
  console.error('未処理の Promise:', reason);
});
```

`process.env` の値は常に文字列なので、数値は `Number` で変換します。終了コード 0 は成功、それ以外はエラーを意味します。

Keywords: process env, exit, uncaught exception, javascript, node.js, js.
