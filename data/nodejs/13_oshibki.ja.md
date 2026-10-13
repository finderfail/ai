# Node.js：エラー処理

エラーは2種類：
- **運用上のエラー**：環境に起因する想定内の問題（ファイルがない、ネットワーク不通、不正な入力）。再試行、4xx/5xx の応答、ユーザーへの通知で対処する。
- **プログラムのエラー**：バグ（`undefined is not a function`、不正な引数）。「握りつぶす」のではなく修正し、プロセスは再起動したほうが安全。

```javascript
try {
  await fsp.readFile(path);
} catch (err) {
  if (err.code === 'ENOENT') return null;
  throw err;
}

throw new Error('注文を保存できませんでした', { cause: err });

process.on('unhandledRejection', (reason) => {
  console.error('未処理の Promise:', reason);
  process.exitCode = 1;
});
process.on('uncaughtException', (err) => {
  console.error('致命的なエラー:', err);
  process.exit(1);
});
```

- メッセージの文字列ではなく `err.code`（`ENOENT`、`EACCES`、`ECONNREFUSED`、`ETIMEDOUT`）で判定する。
- 元のエラーを残すには `cause` を使う。
- `uncaughtException` の後はプロセスの状態が不明なので、ログを出して終了し、プロセスマネージャーに再起動させる。
