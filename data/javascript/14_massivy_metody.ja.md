# JavaScript の配列メソッド

```javascript
const users = [
  { name: 'Aiko', age: 28, active: true },
  { name: 'Kenji', age: 35, active: false },
  { name: 'Yui', age: 22, active: true }
];

const active = users.filter((u) => u.active);
const names = users.map((u) => u.name);
const totalAge = users.reduce((sum, u) => sum + u.age, 0);
const found = users.find((u) => u.age > 30);
const hasYoung = users.some((u) => u.age < 25);
const allAdults = users.every((u) => u.age >= 18);
const sorted = [...users].sort((a, b) => a.age - b.age);
```

`sort` は元の配列を変更するので、スプレッド構文でコピーしてから使います。比較関数なしの `sort` は文字列として並べるため、`[10, 9, 1].sort()` は `[1, 10, 9]` になります。

Keywords: array methods, map, filter, reduce, find, sort, some, every, javascript, node.js, js.
