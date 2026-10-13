# ストリーム

```javascript
const fs = require('node:fs');
const { pipeline } = require('node:stream/promises');
const zlib = require('node:zlib');

async function compress(input, output) {
  await pipeline(
    fs.createReadStream(input),
    zlib.createGzip(),
    fs.createWriteStream(output)
  );
}

const readable = fs.createReadStream('big.txt', { encoding: 'utf8' });
readable.on('data', (chunk) => console.log(chunk.length));
readable.on('end', () => console.log('完了'));
readable.on('error', (error) => console.error(error));
```

ストリームはファイルを少しずつ処理し、全体をメモリに読み込みません。大きなファイルを扱う唯一の現実的な方法です。

Keywords: streams, pipeline, readable, writable, gzip, javascript, node.js, js.
