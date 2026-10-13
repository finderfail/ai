# Переменные окружения и завершение процесса

```javascript
const port = Number(process.env.PORT) || 3000;
const isProduction = process.env.NODE_ENV === 'production';

if (!process.env.API_KEY) {
  console.error('Не задана переменная API_KEY');
  process.exit(1);
}

process.on('uncaughtException', (error) => {
  console.error('Необработанная ошибка:', error);
  process.exit(1);
});

process.on('unhandledRejection', (reason) => {
  console.error('Необработанный промис:', reason);
});
```

`process.env` всегда содержит строки — числа нужно приводить через `Number`. Код выхода 0 означает успех, любой другой — ошибку.

Keywords: process env, exit, uncaught exception, javascript, node.js, js.
