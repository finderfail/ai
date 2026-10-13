# Node.js: частые ошибки

- **Забытый `await`** — промис вместо значения, ошибки теряются.
- **`async` в `forEach`** — `forEach` не ждёт промисов; используйте `for...of` или `Promise.all`.
- **Синхронные операции в сервере** — `readFileSync` в обработчике блокирует всех клиентов.
- **Необработанное событие `error`** у потока или EventEmitter роняет процесс.
- **Смешивание ESM и CommonJS** — `require is not defined in ES module scope` или `Cannot use import statement outside a module`: проверьте `"type"` в package.json и расширения файлов.
- **`__dirname is not defined`** в ESM — используйте `import.meta.dirname`.
- **Плавающая точка**: `0.1 + 0.2 !== 0.3`; деньги — в целых единицах.
- **Мутация общих объектов** между запросами (глобальные переменные с состоянием пользователя).
- **`EADDRINUSE`** — порт занят; **`EMFILE`** — слишком много открытых файлов.
- **Неверная версия Node** — укажите `"engines"` в package.json и файл `.nvmrc`.
