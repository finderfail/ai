# Express.js：express.Router とモジュール構成

`express.Router()` は独自のルートとミドルウェアを持つミニアプリです。API をファイルごとに分けられます。

`routes/users.js`：
```javascript
const { Router } = require('express');
const controller = require('../controllers/users');

const router = Router();

router.get('/', controller.list);
router.get('/:id', controller.get);
router.post('/', controller.create);
router.delete('/:id', controller.remove);

module.exports = router;
```

`app.js`：
```javascript
const usersRouter = require('./routes/users');

app.use('/api/v1/users', usersRouter);
```

ルーター内のパスは相対的で、`router.get('/:id')` は `/api/v1/users/:id` を処理します。

`Router({ mergeParams: true })` を使うと、`/users/:userId/posts` のような入れ子で親パスのパラメータにアクセスできます。
