# Работа с JSON

```javascript
const obj = { name: 'тест', values: [1, 2, 3] };

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

`JSON.stringify` выбрасывает `undefined`, функции и `Symbol`. Циклические ссылки вызывают ошибку `Converting circular structure to JSON`. Даты превращаются в строки и при обратном разборе остаются строками.

Keywords: json, stringify, parse, serialize, javascript, node.js, js.
