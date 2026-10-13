# JavaScript в Node: от колбэков к async/await

```javascript
const fs = require('node:fs');
fs.readFile('a.txt', 'utf8', (err, data) => {
  if (err) return console.error(err);
  console.log(data);
});

const fsp = require('node:fs/promises');
async function main() {
  try {
    const data = await fsp.readFile('a.txt', 'utf8');
    const [a, b] = await Promise.all([fetchA(), fetchB()]);
  } catch (err) {
    console.error('Ошибка:', err.message);
  }
}
```

- Колбэки в стиле Node: первый аргумент — ошибка (`err`).
- Промисы: `pending` → `fulfilled` или `rejected`. `util.promisify` превращает колбэчную функцию в промис-функцию.
- `await` работает внутри `async`-функций и на верхнем уровне ES-модулей.
- Параллельно: `Promise.all` (падает при первой ошибке), `Promise.allSettled` (результаты всех), `Promise.race`, `Promise.any`.
- `await` в цикле медленнее `Promise.all`, но нужен для зависимых операций.
- Отмена: `AbortController` и `signal` для `fetch`, таймеров, `fs`.
