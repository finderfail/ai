# Express.js: безопасность — helmet, CORS, rate limit

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

- **helmet** — защитные заголовки (CSP, HSTS и др.).
- **cors** — запросы из браузера только с нужных доменов; `origin: '*'` с `credentials: true` не работает.
- **express-rate-limit** — лимит частоты запросов, для логина строже.
- Валидируйте ввод, используйте параметризованный SQL, не отдавайте стек ошибок.
- Секреты храните в переменных окружения, не в коде.
- Регулярно запускайте `npm audit` и обновляйте зависимости.
