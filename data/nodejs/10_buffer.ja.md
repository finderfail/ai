# Node.js：Buffer と文字エンコーディング

`Buffer` は固定長のバイト列（`Uint8Array` のサブクラス）。ファイル、ネットワーク、暗号、バイナリプロトコルで使う。

```javascript
const buf = Buffer.from('こんにちは', 'utf8');
buf.length;                       // 15 バイト（5文字ではない）
buf.toString('hex');
buf.toString('base64');
Buffer.from('44GT44KT', 'base64').toString('utf8');
Buffer.alloc(16);                 // ゼロで埋める
Buffer.concat([buf1, buf2]);
buf.subarray(0, 4);               // コピーなし
Buffer.byteLength('こんにちは');  // 15
```

- 文字数とバイト数は異なる。UTF-8 ではキリル文字や日本語は1文字2〜3バイト。
- ストリームのチャンクを結合するときは、まず `Buffer` を集めてからまとめてデコードする（`Buffer.concat(chunks).toString('utf8')`）。そうしないとチャンクの境界でマルチバイト文字が壊れる。あるいは `{ stream: true }` 付きの `TextDecoder` を使う。
- `Buffer.allocUnsafe` は高速だが、古いメモリの内容が残っている可能性があるのですぐに埋める。
