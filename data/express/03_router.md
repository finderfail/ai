# Express.js: express.Router и модульная структура

`express.Router()` — мини-приложение со своими маршрутами и middleware. Позволяет разнести API по файлам.

`routes/users.js`:
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

`app.js`:
```javascript
const usersRouter = require('./routes/users');

app.use('/api/v1/users', usersRouter);
```

Внутри роутера пути относительные: `router.get('/:id')` обслуживает `/api/v1/users/:id`.

`Router({ mergeParams: true })` даёт доступ к параметрам родительского пути, например для вложенного `/users/:userId/posts`.
