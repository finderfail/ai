# Express.js：入力の検証（zod）

`req.body`、`req.query`、`req.params` を信用しないこと。スキーマで検証すると便利で、たとえば **zod**（`npm install zod`）を使います：

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

代替：`express-validator`、`joi`、`ajv`（JSON Schema）。フィールドごとの分かりやすいエラー一覧付きで 400 を返し、余分なフィールドは捨てる（マスアサインメント対策）。
