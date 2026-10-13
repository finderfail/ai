# Модули: CommonJS и ESM

CommonJS (по умолчанию в `.js`, если в package.json нет `"type": "module"`):

```javascript
const http = require('http');
module.exports = { getSystemInfo };
```

ESM (при `"type": "module"` в package.json или в файлах `.mjs`):

```javascript
import http from 'node:http';
export { getSystemInfo };
```

Смешивать их в одном файле нельзя. Префикс `node:` явно указывает на встроенный модуль и защищает от подмены пакетом с тем же именем.

Keywords: module, require, import, export, commonjs, esm, javascript, node.js, js.
