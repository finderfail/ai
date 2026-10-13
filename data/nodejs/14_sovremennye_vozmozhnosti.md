# Node.js: современные встроенные возможности

Многое, для чего раньше ставили пакеты, теперь есть в Node:
- `node --watch app.js` — перезапуск при изменениях (вместо nodemon).
- `node --env-file=.env app.js` — загрузка переменных окружения (вместо dotenv), с Node 20.6.
- `node --test` и `node:test` + `node:assert` — тесты без Jest/Mocha.
- Глобальные `fetch`, `FormData`, `Headers`, `AbortController`, `WebSocket` (клиент, в новых версиях).
- `structuredClone`, `crypto.randomUUID()`, `URL`, `URLSearchParams`.
- `node:readline/promises`, `node:timers/promises` (`await setTimeout(1000)`).
- `util.parseArgs` — разбор аргументов командной строки.
- `import.meta.dirname`, `import.meta.filename` в ES-модулях.
- **TypeScript**: новые версии Node запускают `.ts`, вырезая типы (type stripping); `enum` и подобное — не полностью, проверка типов — через `tsc`.

Конкретная версия появления функции — в документации Node (nodejs.org/docs).
