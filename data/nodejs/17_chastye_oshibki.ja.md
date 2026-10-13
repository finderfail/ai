# Node.js：よくあるミス

- **`await` の付け忘れ**：値ではなく Promise が返り、エラーが「消える」。（TypeScript で）ESLint の `no-floating-promises` を有効にする。
- **`forEach` 内の `async`**：`forEach` は Promise を待たない。`for...of` か `Promise.all` を使う。
- **サーバー内の同期処理**：ハンドラー内の `readFileSync` は全クライアントを止める。
- **未処理の `error` イベント**：ストリームや EventEmitter のものはプロセスを落とす。
- **ESM と CommonJS の混在**：`require is not defined in ES module scope` や `Cannot use import statement outside a module`。package.json の `"type"` と拡張子を確認する。
- ESM での **`__dirname is not defined`**：`import.meta.dirname` を使う。
- **浮動小数点**：`0.1 + 0.2 !== 0.3`。金額は整数の単位で扱う。
- リクエスト間で **共有オブジェクトを変更** する（ユーザーの状態を持つグローバル変数）。
- **`EADDRINUSE`**：ポート使用中。**`EMFILE`**：開いているファイルが多すぎる。ディスクリプタを閉じ、ストリームを使う。
- **Node のバージョン違い**：package.json の `"engines"` と `.nvmrc` ファイルで指定する。
