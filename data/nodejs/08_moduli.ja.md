# Node.js：ES モジュールと CommonJS

**CommonJS**（`"type": "module"` のない `.js` の既定、および `.cjs`）：
```javascript
const path = require('node:path');
module.exports = { helper };
```

**ES モジュール**（package.json の `"type": "module"`、または `.mjs` ファイル）：
```javascript
import path from 'node:path';
import { readFile } from 'node:fs/promises';
export function helper() {}
export default app;
const config = JSON.parse(await readFile(new URL('./config.json', import.meta.url), 'utf8'));
```

違い：
- ESM には `__dirname` と `require` がない。`import.meta.dirname` / `import.meta.filename`（新しい Node）か `fileURLToPath(import.meta.url)` を使う。
- ESM では相対インポートに拡張子が必須：`./utils.js`。
- ESM ではトップレベル `await` が使える。
- ESM から CommonJS パッケージをインポートできる。新しい Node では同期的な ES モジュールの `require()` もできる。
- package.json の `"exports"` フィールドで、パッケージ外から使えるファイルを決める。

新しいプロジェクトでは ESM が推奨。
