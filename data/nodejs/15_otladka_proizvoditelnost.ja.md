# Node.js：デバッグとパフォーマンス

**デバッグ**
- `node --inspect app.js`（最初の行で止めるなら `--inspect-brk`）と、Chrome の `chrome://inspect` または VS Code のデバッガー。
- コード内の `debugger;` でブレークポイント。
- `console.table`、`console.time` / `console.timeEnd`、`util.inspect(obj, { depth: null })`。

**プロファイリング**
- `node --cpu-prof app.js`：Chrome DevTools 用の CPU プロファイル。
- `node --heapsnapshot-signal=SIGUSR2` とヒープスナップショットでメモリリークを探す。
- 正確な計測には `perf_hooks.performance.now()`。
- `autocannon` や `k6`：HTTP の負荷テスト。

**遅くなるよくある原因**
- リクエストハンドラー内の同期処理（`*Sync`、重い `JSON`）。
- `Promise.all` で済むところでの逐次 `await`。
- データベースへの N+1 クエリ。
- DB のコネクションプールや外部 HTTP の keep-alive がない。
- メモリリーク：上限のないグローバルキャッシュ、解除されないイベントハンドラー、タイマー。
