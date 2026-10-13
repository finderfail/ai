# Node.js: отладка и производительность

**Отладка**
- `node --inspect app.js` (или `--inspect-brk`, чтобы остановиться на первой строке) и `chrome://inspect` в Chrome либо отладчик VS Code.
- `debugger;` в коде ставит точку останова.
- `console.table`, `console.time` / `console.timeEnd`, `util.inspect(obj, { depth: null })`.

**Профилирование**
- `node --cpu-prof app.js` — CPU-профиль для Chrome DevTools.
- `node --heapsnapshot-signal=SIGUSR2` и снимки памяти для поиска утечек.
- `perf_hooks.performance.now()` для точных замеров.
- `autocannon` или `k6` — нагрузочное тестирование HTTP.

**Частые причины медленной работы**
- Синхронные операции (`*Sync`, тяжёлый `JSON`) в обработчиках запросов.
- Последовательные `await` там, где можно `Promise.all`.
- N+1 запросов к базе данных.
- Отсутствие пула соединений к БД и keep-alive для исходящих HTTP.
- Утечки памяти: растущие глобальные кеши без лимита, неотписанные обработчики событий, таймеры.
