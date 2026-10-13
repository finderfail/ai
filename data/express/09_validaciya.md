# Express.js: валидация входных данных (zod)

Никогда не доверяйте `req.body`, `req.query`, `req.params`. Удобно валидировать схемой, например библиотекой **zod** (`npm install zod`):

```javascript
const { z } = require('zod');

const createUser = z.object({
  email: z.string().email(),
  name: z.string().min(1).max(100),
  age: z.coerce.number().int().min(0).optional()
});

function validate(schema, source = 'body') {
  return (req, res, next) => {
    const result = schema.safeParse(req[source]);
    if (!result.success) {
      return res.status(400).json({ error: 'Validation failed', details: result.error.issues });
    }
    req.validated = result.data;
    next();
  };
}

app.post('/users', validate(createUser), (req, res) => {
  res.status(201).json(req.validated);
});
```

Альтернативы: `express-validator`, `joi`, `ajv` (JSON Schema). Возвращайте 400 с понятным списком ошибок по полям, а лишние поля отбрасывайте — защита от mass assignment.
