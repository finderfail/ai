# Express.js：supertest によるテスト

```bash
npm install --save-dev supertest
```

```javascript
const test = require('node:test');
const assert = require('node:assert/strict');
const request = require('supertest');
const app = require('../src/app');

test('GET /health は ok を返す', async () => {
  const res = await request(app).get('/health');
  assert.equal(res.status, 200);
  assert.deepEqual(res.body, { status: 'ok' });
});

test('POST /users はメールを検証する', async () => {
  const res = await request(app)
    .post('/api/v1/users')
    .send({ email: 'not-email', name: 'Aiko' })
    .set('Authorization', `Bearer ${token}`);
  assert.equal(res.status, 400);
});
```

実行：`node --test`。supertest は一時的なポートでアプリを起動するため、`app.js` は `listen` を呼ばずに `app` をエクスポートしておく。

分離のため、データベースはテスト用 DB かリポジトリのインメモリ実装に置き換える。
