# Обработка ошибок

```javascript
class ValidationError extends Error {
  constructor(message, field) {
    super(message);
    this.name = 'ValidationError';
    this.field = field;
  }
}

async function handle(payload) {
  try {
    if (!payload.email) {
      throw new ValidationError('Email обязателен', 'email');
    }
    return await save(payload);
  } catch (error) {
    if (error instanceof ValidationError) {
      return { ok: false, field: error.field, message: error.message };
    }
    throw error;
  } finally {
    console.log('запрос обработан');
  }
}
```

`finally` выполняется всегда, включая случаи с `return` внутри `try` или `catch`. Не глотайте неизвестные ошибки — пробрасывайте их дальше.

Keywords: error, exception, try catch, throw, custom error, javascript, node.js, js.
