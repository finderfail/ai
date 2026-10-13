# JavaScript：型と型変換

プリミティブ：`string`、`number`（64ビット浮動小数点）、`bigint`、`boolean`、`undefined`、`null`、`symbol`。それ以外はすべてオブジェクト（配列、関数、日付）。

```javascript
typeof 'a';        // 'string'
typeof null;       // 'object' — 言語の歴史的な誤り
Array.isArray([]); // true
Number.isInteger(5.0);
0.1 + 0.2;         // 0.30000000000000004
Number.MAX_SAFE_INTEGER; // 9007199254740991。それ以上は BigInt：10n ** 20n
```

**比較**：常に `===` と `!==` を使う。`==` は型を変換する：`'' == 0` や `null == undefined` は true。

**偽となる値（falsy）**：`false`、`0`、`-0`、`0n`、`''`、`null`、`undefined`、`NaN`。それ以外は `'0'`、`[]`、`{}` も含めて真。

**明示的な変換**：`Number('42')`、`parseInt('42px', 10)`、`String(42)`、`Boolean(x)`。`Number('')` は 0、`Number('abc')` は `NaN`。判定は `Number.isNaN()`。

金額を浮動小数点で持たないこと。最小単位の整数か BigInt を使う。
