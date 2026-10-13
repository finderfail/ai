# Работа с файлами

```javascript
const fs = require('fs');
const fsp = require('fs/promises');

const text = fs.readFileSync('config.json', 'utf8');
const data = JSON.parse(text);

async function save(path, obj) {
  await fsp.writeFile(path, JSON.stringify(obj, null, 2), 'utf8');
}
```

Синхронные функции (`readFileSync`) блокируют цикл событий — в обработчиках запросов используют асинхронные версии из `fs/promises`.

Keywords: file, read file, write file, fs module, javascript, node.js, js.
