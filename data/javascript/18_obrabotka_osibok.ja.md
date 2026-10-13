# エラー処理

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
      throw new ValidationError('メールアドレスは必須です', 'email');
    }
    return await save(payload);
  } catch (error) {
    if (error instanceof ValidationError) {
      return { ok: false, field: error.field, message: error.message };
    }
    throw error;
  } finally {
    console.log('リクエスト処理完了');
  }
}
```

`finally` は `try` や `catch` の中で `return` した場合も含め、常に実行されます。想定外のエラーは握りつぶさず、そのまま投げ直しましょう。

Keywords: error, exception, try catch, throw, custom error, javascript, node.js, js.
