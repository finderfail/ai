# JavaScript：関数、アロー関数、クロージャ、this

```javascript
function sum(a, b = 0, ...rest) {
  return a + b + rest.reduce((s, x) => s + x, 0);
}

const double = (x) => x * 2;

function counter() {
  let value = 0;
  return () => ++value;
}
const next = counter();
next(); next();
```

- **デフォルト引数** と **残余引数**（`...rest`）が `arguments` の代わりになる。
- **クロージャ**：関数は作られたスコープの変数を「覚えている」（例の `value` は呼び出しの間も残る）。プライベートな状態、ファクトリー、メモ化の基礎。
- 通常の関数の **this** は呼び出し方で決まる（`obj.method()` → `obj`、単なる `fn()` → strict モードでは `undefined`）。アロー関数は自分の `this` を持たず外側のスコープから取るので、コールバックで便利。
- `fn.bind(obj)`、`fn.call(obj, a)`、`fn.apply(obj, [a])` で `this` を明示する。
- 関数は第一級オブジェクトで、渡したり返したり変数に入れたりできる。
