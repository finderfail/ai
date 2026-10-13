# Потоки (streams)

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
readable.on('end', () => console.log('готово'));
readable.on('error', (error) => console.error(error));
```

Потоки обрабатывают файл по кусочкам и не загружают его целиком в память — это единственный разумный способ работать с большими файлами.

Keywords: streams, pipeline, readable, writable, gzip, javascript, node.js, js.
