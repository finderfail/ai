# Express.js：セキュリティ — helmet、CORS、レート制限

```javascript
const helmet = require('helmet');
const cors = require('cors');
const rateLimit = require('express-rate-limit');

app.disable('x-powered-by');
app.set('trust proxy', 1);
app.use(helmet());
app.use(cors({ origin: ['https://app.example.com'], credentials: true }));
app.use(express.json({ limit: '100kb' }));
app.use('/api', rateLimit({ windowMs: 60_000, limit: 100, standardHeaders: true, legacyHeaders: false }));
app.use('/auth/login', rateLimit({ windowMs: 15 * 60_000, limit: 10 }));
```

- **helmet**：保護用のヘッダー（CSP、X-Content-Type-Options、HSTS など）を設定。
- **cors**：ブラウザからのリクエストを必要なドメインだけに許可。`origin: '*'` と `credentials: true` の組み合わせは動作せず、安全でもない。
- **express-rate-limit**：リクエスト頻度を制限。ログインはより厳しくする。
- 入力を検証し、パラメータ化 SQL を使い、エラーのスタックを返さない。
- 秘密情報はコードではなく環境変数に。
- `npm audit` を定期的に実行し、依存関係を更新する。
