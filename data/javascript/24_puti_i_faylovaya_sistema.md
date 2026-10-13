# Пути и файловая система

```javascript
const path = require('node:path');
const fs = require('node:fs');

const full = path.join(__dirname, 'data', 'config.json');
const ext = path.extname(full);
const base = path.basename(full, '.json');
const dir = path.dirname(full);

if (fs.existsSync(dir)) {
  const files = fs.readdirSync(dir).filter((f) => f.endsWith('.json'));
}

fs.mkdirSync(path.join(dir, 'nested'), { recursive: true });
```

`path.join` сам подставляет правильный разделитель для ОС. В ESM `__dirname` недоступен — его получают через `path.dirname(fileURLToPath(import.meta.url))`.

Keywords: path, join, dirname, basename, directory, javascript, node.js, js.
