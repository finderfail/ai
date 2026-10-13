# Перебор массива: forEach и циклы — часть 2

## Другие способы

```javascript
for (let i = 0; i < users.length; i++) {
  console.log(users[i]);
}

const upper = users.map((name) => name.toUpperCase());

for (const key in { a: 1, b: 2 }) {
  console.log(key);
}
```

`for...in` перебирает **ключи объекта**, а не значения массива — для массивов его не используют. `map` возвращает новый массив, `forEach` — нет.

## forEach и async

`forEach` не ждёт асинхронные колбэки:

```javascript
for (const name of users) {
  await save(name);
}

await Promise.all(users.map((name) => save(name)));
```

Первый вариант выполняет по очереди, второй — параллельно. `users.forEach(async ...)` не дождётся завершения.

Keywords: forEach, for of, for in, loop, iterate, array iteration, перебор массива, цикл по массиву, итерация.
