# Хеширование и случайные значения

```javascript
const crypto = require('node:crypto');

const hash = crypto.createHash('sha256').update('текст').digest('hex');
const token = crypto.randomBytes(32).toString('hex');
const uuid = crypto.randomUUID();

function hashPassword(password, salt) {
  return crypto.scryptSync(password, salt, 32).toString('hex');
}

const salt = crypto.randomBytes(16).toString('hex');
const stored = hashPassword('secret123', salt);
```

Для паролей нельзя использовать простой sha256 — нужен медленный алгоритм с солью: `scrypt`, `bcrypt` или `argon2`. Для токенов берите `crypto.randomBytes`, а не `Math.random`.

Keywords: hash, crypto, random, uuid, sha256, password, javascript, node.js, js.
