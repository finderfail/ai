# Node.js：イベントループ

実行の順序：
1. 現在のタスクの同期コードをすべて実行。
2. **マイクロタスク**：まず `process.nextTick` のキュー、次に Promise（`.then`、`await`）。
3. libuv のフェーズ：**timers**（`setTimeout`、`setInterval`）→ pending callbacks → **poll**（I/O の待機と処理）→ **check**（`setImmediate`）→ close callbacks。各コールバックの後にもマイクロタスクが実行される。

```javascript
setTimeout(() => console.log('timeout'), 0);
setImmediate(() => console.log('immediate'));
Promise.resolve().then(() => console.log('promise'));
process.nextTick(() => console.log('nextTick'));
console.log('sync');
```
出力：`sync`、`nextTick`、`promise`、その後 `timeout` と `immediate`（メインモジュールでは順序は保証されない。I/O のコールバック内では `setImmediate` が常に先）。

**ループを止めないこと**：長いループ、巨大な文字列の `JSON.parse`、ハンドラー内の同期 `fs.*Sync`、複雑な正規表現（ReDoS）は全リクエストの処理を止める。重い処理は `worker_threads` へ。
