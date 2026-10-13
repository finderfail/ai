# Тесты встроенным модулем node:test

```javascript
const test = require('node:test');
const assert = require('node:assert/strict');

test('сложение работает', () => {
  assert.equal(2 + 2, 4);
});

test('асинхронный код', async () => {
  const result = await Promise.resolve(42);
  assert.equal(result, 42);
});

test('объекты сравниваются по значению', () => {
  assert.deepEqual({ a: 1 }, { a: 1 });
});
```

Запуск: `node --test`. Модуль `node:test` встроен начиная с Node.js 18, внешних библиотек не требуется.

Keywords: test, testing, assert, unit test, javascript, node.js, js.
