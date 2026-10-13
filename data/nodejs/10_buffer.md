# Node.js: Buffer и кодировки

`Buffer` — последовательность байтов фиксированной длины (подкласс `Uint8Array`). Нужен для файлов, сети, криптографии, двоичных протоколов.

```javascript
const buf = Buffer.from('Привет', 'utf8');
buf.length;                       // 12 байт, а не 6 символов
buf.toString('hex');
buf.toString('base64');
Buffer.from('UHJpdmV0', 'base64').toString('utf8');
Buffer.alloc(16);                 // заполнен нулями
Buffer.concat([buf1, buf2]);
buf.subarray(0, 4);               // без копирования
Buffer.byteLength('Привет');      // 12
```

- Длина строки в символах и в байтах отличается: кириллица и японский занимают 2–3 байта на символ в UTF-8.
- При склейке потоковых чанков сначала собирайте `Buffer`'ы и декодируйте целиком (`Buffer.concat(chunks).toString('utf8')`), иначе многобайтовый символ разорвётся на границе чанка. Либо используйте `TextDecoder` с `{ stream: true }`.
- `Buffer.allocUnsafe` быстрее, но содержит мусор — заполняйте сразу.
