# Node の JavaScript：コールバックから async/await へ

```javascript
const fs = require('node:fs');
fs.readFile('a.txt', 'utf8', (err, data) => {
  if (err) return console.error(err);
  console.log(data);
});

const fsp = require('node:fs/promises');
async function main() {
  try {
    const data = await fsp.readFile('a.txt', 'utf8');
    const [a, b] = await Promise.all([fetchA(), fetchB()]);
  } catch (err) {
    console.error('エラー:', err.message);
  }
}
```

- Node 形式のコールバック：最初の引数はエラー（`err`）。
- Promise：`pending` → `fulfilled` か `rejected`。`util.promisify` でコールバック関数を Promise 関数に変換できる。
- `await` は `async` 関数の中と、ES モジュールのトップレベルで使える。
- 並列：`Promise.all`（最初のエラーで失敗）、`Promise.allSettled`（すべての結果）、`Promise.race`、`Promise.any`。
- ループ内の逐次 `await` は `Promise.all` より遅いが、処理が互いに依存する場合や負荷を抑えたい場合に必要。
- キャンセル：`fetch`、タイマー、`fs` に `AbortController` と `signal` を使う。
