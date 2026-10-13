# Node.js: обработка ошибок

Два вида ошибок:
- **Операционные** — нет файла, сеть недоступна, неверный ввод. Их обрабатывают.
- **Программные** — баги. Их исправляют, процесс безопаснее перезапустить.

```javascript
try {
  await fsp.readFile(path);
} catch (err) {
  if (err.code === 'ENOENT') return null;
  throw err;
}

throw new Error('Не удалось сохранить заказ', { cause: err });

process.on('unhandledRejection', (reason) => {
  console.error('Необработанный промис:', reason);
  process.exitCode = 1;
});
process.on('uncaughtException', (err) => {
  console.error('Критическая ошибка:', err);
  process.exit(1);
});
```

- Проверяйте `err.code` (`ENOENT`, `EACCES`, `ECONNREFUSED`, `ETIMEDOUT`), а не текст сообщения.
- Используйте `cause`, чтобы сохранить исходную ошибку.
- После `uncaughtException` состояние процесса неизвестно — логируйте и завершайте, менеджер процессов перезапустит.
