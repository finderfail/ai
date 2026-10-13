# Аргументы командной строки и переменные окружения

```javascript
const args = process.argv.slice(2);
const command = args[0];

const port = process.env.PORT || 3000;
const apiKey = process.env.API_KEY;

if (!apiKey) {
  console.error('Не задана переменная окружения API_KEY');
  process.exit(1);
}
```

`process.argv[0]` — путь к Node.js, `process.argv[1]` — путь к скрипту, поэтому пользовательские аргументы начинаются с индекса 2.

Keywords: argv, command line arguments, env, environment variables, javascript, node.js, js.
