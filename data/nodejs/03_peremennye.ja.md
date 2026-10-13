# JavaScript：変数、スコープ、巻き上げ

```javascript
const PORT = 3000;
let count = 0;
var legacy = 'var は使わない';
```

- **const**：再代入できない（中のオブジェクトは変更可能：`const a = []; a.push(1)` は動く）。基本はこれを使う。
- **let**：値を変える変数。
- **var**：古い書き方。スコープがブロックではなく関数で、`undefined` として「巻き上げ」られる。

スコープ：グローバル、モジュール（ファイルごと）、関数、`let`/`const` の **ブロック**（`{ }`、`if`、`for`）。

**巻き上げ（hoisting）**：宣言はスコープの先頭に持ち上げられる。`function` 宣言は宣言前でも使える。`let`/`const` は宣言前は「一時的デッドゾーン」（TDZ）にあり、参照すると `ReferenceError`。

```javascript
for (let i = 0; i < 3; i++) setTimeout(() => console.log(i));
```
0、1、2 と出力される。`var` なら 3、3、3 になる（ループ内クロージャの典型的なミス）。
