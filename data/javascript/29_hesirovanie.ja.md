# ハッシュと乱数

```javascript
const crypto = require('node:crypto');

const hash = crypto.createHash('sha256').update('テキスト').digest('hex');
const token = crypto.randomBytes(32).toString('hex');
const uuid = crypto.randomUUID();

function hashPassword(password, salt) {
  return crypto.scryptSync(password, salt, 32).toString('hex');
}

const salt = crypto.randomBytes(16).toString('hex');
const stored = hashPassword('secret123', salt);
```

パスワードに単純な sha256 は使えません。ソルト付きの低速なアルゴリズム（`scrypt`、`bcrypt`、`argon2`）が必要です。トークンには `Math.random` ではなく `crypto.randomBytes` を使います。

Keywords: hash, crypto, random, uuid, sha256, password, javascript, node.js, js.
