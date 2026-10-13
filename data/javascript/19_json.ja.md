# JSON の扱い

```javascript
const obj = { name: 'テスト', values: [1, 2, 3] };

const text = JSON.stringify(obj);
const pretty = JSON.stringify(obj, null, 2);
const parsed = JSON.parse(text);

function safeParse(raw, fallback = null) {
  try {
    return JSON.parse(raw);
  } catch (_) {
    return fallback;
  }
}
```

`JSON.stringify` は `undefined`、関数、`Symbol` を出力から除外します。循環参照があると `Converting circular structure to JSON` エラーになります。日付は文字列に変換され、解析し直しても文字列のままです。

Keywords: json, stringify, parse, serialize, javascript, node.js, js.
