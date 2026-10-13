# モジュール：CommonJS と ESM

CommonJS（package.json に `"type": "module"` がない場合の `.js` の既定）：

```javascript
const http = require('http');
module.exports = { getSystemInfo };
```

ESM（package.json に `"type": "module"` がある場合、または `.mjs` ファイル）：

```javascript
import http from 'node:http';
export { getSystemInfo };
```

1つのファイルで両方を混ぜることはできません。`node:` 接頭辞は組み込みモジュールであることを明示し、同名のパッケージによるすり替えを防ぎます。

Keywords: module, require, import, export, commonjs, esm, javascript, node.js, js.
