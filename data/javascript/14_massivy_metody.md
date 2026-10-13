# Методы массивов в JavaScript

```javascript
const users = [
  { name: 'Аня', age: 28, active: true },
  { name: 'Борис', age: 35, active: false },
  { name: 'Вера', age: 22, active: true }
];

const active = users.filter((u) => u.active);
const names = users.map((u) => u.name);
const totalAge = users.reduce((sum, u) => sum + u.age, 0);
const found = users.find((u) => u.age > 30);
const hasYoung = users.some((u) => u.age < 25);
const allAdults = users.every((u) => u.age >= 18);
const sorted = [...users].sort((a, b) => a.age - b.age);
```

`sort` меняет исходный массив, поэтому его копируют через spread. `sort` без функции сравнения сортирует как строки: `[10, 9, 1].sort()` даст `[1, 10, 9]`.

Keywords: array methods, map, filter, reduce, find, sort, some, every, javascript, node.js, js.
