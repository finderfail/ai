# Асинхронность: промисы и async/await

```javascript
async function main() {
  try {
    const [users, posts] = await Promise.all([
      fetch('/api/users').then((r) => r.json()),
      fetch('/api/posts').then((r) => r.json())
    ]);
    console.log(users.length, posts.length);
  } catch (error) {
    console.error('Ошибка:', error.message);
  }
}
```

`Promise.all` выполняет запросы параллельно и падает, если упал хотя бы один. `Promise.allSettled` возвращает результаты всех, включая отклонённые.

Keywords: async, await, promise, promises, asynchronous, javascript, node.js, js.
