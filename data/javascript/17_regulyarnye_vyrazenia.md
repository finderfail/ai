# Регулярные выражения

```javascript
const emailRe = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;
const isEmail = emailRe.test('user@example.com');

const text = 'заказ 123, заказ 456';
const numbers = text.match(/\d+/g);

const withGroups = '2026-08-20'.match(/(\d{4})-(\d{2})-(\d{2})/);
const [, year, month, day] = withGroups;

const named = '2026-08-20'.match(/(?<year>\d{4})-(?<month>\d{2})/);
console.log(named.groups.year);

const replaced = 'привет мир'.replace(/(\w+) (\w+)/u, '$2 $1');
```

Флаг `g` возвращает все совпадения, без него — только первое. Для кириллицы полезен флаг `u`.

Keywords: regex, regular expression, match, test, pattern, javascript, node.js, js.
