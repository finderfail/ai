# Node.js：コードのセキュリティ

- **コマンドインジェクション**：ユーザー入力を `exec` に渡さない。引数を配列で渡す `execFile`/`spawn` を使う。
- **パストラバーサル**：リクエスト由来のパス（`../../etc/passwd`）は正規化し、許可したフォルダ内か確認する：
```javascript
const full = path.resolve(BASE_DIR, userPath);
if (!full.startsWith(BASE_DIR + path.sep)) throw new Error('アクセス禁止');
```
- **プロトタイプ汚染**：`__proto__`、`constructor` などのキーを含む未検証の JSON をオブジェクトにマージしない。辞書には `Object.create(null)` か `Map` を使い、スキーマで検証する。
- 外部データでの **eval や new Function** は絶対に使わない。
- **ReDoS**：ユーザー入力に複雑な正規表現を使うとイベントループが止まることがある。入力の長さを制限する。
- **依存関係**：`npm audit`、lock ファイル、`npm ci`。知らないパッケージの `postinstall` スクリプトに注意し、名前（タイポスクワッティング）を確認する。
- **秘密情報** は環境変数に置き、比較には `crypto.timingSafeEqual` を使う。
- プロセスを root で動かさない。
