# Базовая безопасность HTTP-сервера

```javascript
const crypto = require('node:crypto');

function safeCompare(a, b) {
  const bufA = Buffer.from(a);
  const bufB = Buffer.from(b);
  if (bufA.length !== bufB.length) return false;
  return crypto.timingSafeEqual(bufA, bufB);
}

function checkAuth(req) {
  const header = req.headers.authorization || '';
  if (!header.startsWith('Bearer ')) return false;
  return safeCompare(header.slice(7), process.env.API_KEY);
}

function escapeHtml(str) {
  return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}
```

Сравнивать секреты обычным `===` небезопасно — используйте `crypto.timingSafeEqual`. Никогда не вставляйте пользовательский ввод в HTML без экранирования.

Keywords: security, auth header, timing safe, escape html, javascript, node.js, js.
