# パスとファイルシステム

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

`path.join` は OS に合った区切り文字を自動で使います。ESM では `__dirname` が使えないので、`path.dirname(fileURLToPath(import.meta.url))` で取得します。

Keywords: path, join, dirname, basename, directory, javascript, node.js, js.
