# Node.js：最近の組み込み機能

以前はパッケージが必要だった多くの機能が、Node に組み込まれている：
- `node --watch app.js`：変更時に再起動（nodemon の代わり）。
- `node --env-file=.env app.js`：環境変数の読み込み（dotenv の代わり）。Node 20.6 以降。
- `node --test` と `node:test` + `node:assert`：Jest/Mocha なしでテスト。
- グローバルな `fetch`、`FormData`、`Headers`、`AbortController`、`WebSocket`（クライアント、新しいバージョン）。
- `structuredClone`、`crypto.randomUUID()`、`URL`、`URLSearchParams`。
- `node:readline/promises`、`node:timers/promises`（`await setTimeout(1000)`）。
- `util.parseArgs`：コマンドライン引数の解析。
- ES モジュールの `import.meta.dirname`、`import.meta.filename`。
- **TypeScript**：新しい Node は型注釈を取り除くだけで `.ts` ファイルを実行できる（type stripping）。コンパイルが必要な構文（`enum` など）は完全には対応していない。型チェックは引き続き `tsc` で行う。

各機能が追加された正確なバージョンは Node のドキュメント（nodejs.org/docs）で確認する。
