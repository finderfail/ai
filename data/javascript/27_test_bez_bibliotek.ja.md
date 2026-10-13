# 組み込みモジュール node:test によるテスト

```javascript
const test = require('node:test');
const assert = require('node:assert/strict');

test('足し算が動く', () => {
  assert.equal(2 + 2, 4);
});

test('非同期コード', async () => {
  const result = await Promise.resolve(42);
  assert.equal(result, 42);
});

test('オブジェクトは値で比較される', () => {
  assert.deepEqual({ a: 1 }, { a: 1 });
});
```

実行：`node --test`。`node:test` は Node.js 18 から組み込まれており、外部ライブラリは不要です。

Keywords: test, testing, assert, unit test, javascript, node.js, js.
