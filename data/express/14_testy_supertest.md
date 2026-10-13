# Express.js: тестирование с supertest

```bash
npm install --save-dev supertest
```

```javascript
const test = require('node:test');
const assert = require('node:assert/strict');
const request = require('supertest');
const app = require('../src/app');

test('GET /health отвечает ok', async () => {
  const res = await request(app).get('/health');
  assert.equal(res.status, 200);
  assert.deepEqual(res.body, { status: 'ok' });
});

test('POST /users валидирует email', async () => {
  const res = await request(app)
    .post('/api/v1/users')
    .send({ email: 'не-почта', name: 'Аня' })
    .set('Authorization', `Bearer ${token}`);
  assert.equal(res.status, 400);
});
```

Запуск: `node --test`. supertest сам поднимает приложение на временном порту — важно, чтобы `app.js` экспортировал `app` без вызова `listen`.

Для изоляции подменяйте БД тестовой базой или in-memory реализацией репозитория.
