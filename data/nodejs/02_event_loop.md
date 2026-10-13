# Node.js: цикл событий (event loop)

Порядок выполнения:
1. Весь синхронный код текущей задачи.
2. **Микрозадачи**: сначала очередь `process.nextTick`, затем промисы (`.then`, `await`).
3. Фазы цикла libuv: **timers** (`setTimeout`, `setInterval`) → pending callbacks → **poll** (ожидание и обработка I/O) → **check** (`setImmediate`) → close callbacks. После каждого колбэка снова выполняются микрозадачи.

```javascript
setTimeout(() => console.log('timeout'), 0);
setImmediate(() => console.log('immediate'));
Promise.resolve().then(() => console.log('promise'));
process.nextTick(() => console.log('nextTick'));
console.log('sync');
```
Вывод: `sync`, `nextTick`, `promise`, затем `timeout` и `immediate` (их порядок в главном модуле не гарантирован; внутри I/O-колбэка `setImmediate` всегда раньше).

**Не блокируйте цикл**: долгие циклы, `JSON.parse` огромных строк, `fs.*Sync` в обработчиках, тяжёлые регулярки (ReDoS) останавливают все запросы. Тяжёлое — в `worker_threads`.
