# ファイル操作

```javascript
const fs = require('fs');
const fsp = require('fs/promises');

const text = fs.readFileSync('config.json', 'utf8');
const data = JSON.parse(text);

async function save(path, obj) {
  await fsp.writeFile(path, JSON.stringify(obj, null, 2), 'utf8');
}
```

同期関数（`readFileSync`）はイベントループをブロックします。リクエストのハンドラー内では `fs/promises` の非同期版を使います。

Keywords: file, read file, write file, fs module, javascript, node.js, js.
