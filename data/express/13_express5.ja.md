# Express.js：Express 5 の変更点

- **Node.js 18 以上** が必要。
- **async のエラー**：`async` ハンドラーの拒否された Promise や `throw` は自動でエラーハンドラーへ渡る。
- **新しいパス構文**（path-to-regexp 8）：
  - ワイルドカードには名前が必要：`/files/*` ではなく `/files/*splat`；
  - 省略可能な部分は波かっこ：`/users/:id?` ではなく `/users{/:id}`；
  - パス文字列内の正規表現は使えなくなった。
- `req.query` は読み取り専用で、クエリパーサーの既定は「simple」。
- `express.urlencoded()` の既定は `extended: false`。
- 非推奨メソッドの削除：`app.del` → `app.delete`、`res.sendfile` → `res.sendFile`、`req.param()` → `req.params` / `req.query` / `req.body`、`res.send(status, body)` → `res.status(status).send(body)`。
- `res.redirect('back')` は削除。`req.get('Referrer') || '/'` を使う。
- `res.status()` は 100〜999 の整数のみ。

移行：`npm install express@5`、`*` と `?` を含むパスを修正し、テストを実行する。
