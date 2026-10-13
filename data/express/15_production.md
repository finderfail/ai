# Express.js: запуск в продакшене

```javascript
const server = app.listen(PORT);

function shutdown(signal) {
  console.log(`${signal}: останавливаюсь`);
  server.close(() => process.exit(0));
  setTimeout(() => process.exit(1), 10_000).unref();
}

process.on('SIGTERM', shutdown);
process.on('SIGINT', shutdown);
```

Чек-лист:
- `NODE_ENV=production` — Express включает кеширование шаблонов и менее подробные ошибки.
- За nginx/Caddy/балансировщиком: `app.set('trust proxy', 1)`.
- TLS завершать на обратном прокси; Express слушает localhost.
- Логи в stdout в JSON (pino), без console.log в горячих местах.
- Менеджер процессов: systemd, Docker (`restart: unless-stopped`) или PM2.
- Health-check эндпоинт `/health` для балансировщика.
- Включить сжатие (`compression`) или отдать это прокси.
- Конфигурация только через переменные окружения (`node --env-file=.env` в Node 20.6+).
