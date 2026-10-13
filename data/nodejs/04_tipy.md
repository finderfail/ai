# JavaScript: типы и приведение типов

Примитивы: `string`, `number` (64-битный float), `bigint`, `boolean`, `undefined`, `null`, `symbol`. Всё остальное — объекты (массивы, функции, даты).

```javascript
typeof 'a';        // 'string'
typeof null;       // 'object' — историческая ошибка языка
Array.isArray([]); // true
Number.isInteger(5.0);
0.1 + 0.2;         // 0.30000000000000004
Number.MAX_SAFE_INTEGER; // 9007199254740991, дальше — BigInt: 10n ** 20n
```

**Сравнение**: всегда используйте `===` и `!==`. `==` приводит типы: `'' == 0` и `null == undefined` — true.

**Ложные значения**: `false`, `0`, `-0`, `0n`, `''`, `null`, `undefined`, `NaN`. Всё остальное истинно, включая `'0'`, `[]` и `{}`.

**Явное приведение**: `Number('42')`, `parseInt('42px', 10)`, `String(42)`, `Boolean(x)`. `Number('')` даёт 0, `Number('abc')` — `NaN`; проверка — `Number.isNaN()`.

Деньги не храните во float: используйте целые минимальные единицы или BigInt.
