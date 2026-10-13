# HTML5：文書の構造

```html
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>ページのタイトル</title>
  <meta name="description" content="検索エンジン向けの短い説明">
  <link rel="icon" href="/favicon.ico">
  <link rel="stylesheet" href="/styles.css">
  <script src="/app.js" defer></script>
</head>
<body>
  <h1>見出し</h1>
</body>
</html>
```

- `<!DOCTYPE html>` は HTML5 の短い文書型宣言で、ブラウザを標準モードにする。
- `<html>` の `lang` は読み上げ、翻訳、SEO に必要。
- `<meta charset="utf-8">` は `<head>` の最初に書く。
- `defer`：スクリプトを並行して読み込み、HTML の解析後に実行。`async`：読み込み次第すぐ実行（順序なし）。
- HTML は現在 WHATWG の「リビングスタンダード」（HTML Living Standard）として発展している。
