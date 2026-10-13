# Node.js: модули ESM и CommonJS

**CommonJS** (по умолчанию для `.js` без `"type": "module"`, и для `.cjs`):
```javascript
const path = require('node:path');
module.exports = { helper };
```

**ES-модули** (`"type": "module"` в package.json или файлы `.mjs`):
```javascript
import path from 'node:path';
import { readFile } from 'node:fs/promises';
export function helper() {}
export default app;
const config = JSON.parse(await readFile(new URL('./config.json', import.meta.url), 'utf8'));
```

Отличия:
- В ESM нет `__dirname` и `require`; используйте `import.meta.dirname` / `import.meta.filename` (в новых версиях Node) или `fileURLToPath(import.meta.url)`.
- В ESM обязательно указывать расширение в относительных импортах: `./utils.js`.
- В ESM доступен `await` на верхнем уровне.
- Из ESM можно импортировать CommonJS-пакеты.
- Поле `"exports"` в package.json определяет, какие файлы пакета доступны снаружи.

Для новых проектов предпочтителен ESM.
