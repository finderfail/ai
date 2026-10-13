# コマンドライン引数と環境変数

```javascript
const args = process.argv.slice(2);
const command = args[0];

const port = process.env.PORT || 3000;
const apiKey = process.env.API_KEY;

if (!apiKey) {
  console.error('環境変数 API_KEY が設定されていません');
  process.exit(1);
}
```

`process.argv[0]` は Node.js のパス、`process.argv[1]` はスクリプトのパスなので、ユーザーの引数はインデックス 2 から始まります。

Keywords: argv, command line arguments, env, environment variables, javascript, node.js, js.
