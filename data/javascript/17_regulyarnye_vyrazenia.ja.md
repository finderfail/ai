# 正規表現

```javascript
const emailRe = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;
const isEmail = emailRe.test('user@example.com');

const text = '注文 123、注文 456';
const numbers = text.match(/\d+/g);

const withGroups = '2026-08-20'.match(/(\d{4})-(\d{2})-(\d{2})/);
const [, year, month, day] = withGroups;

const named = '2026-08-20'.match(/(?<year>\d{4})-(?<month>\d{2})/);
console.log(named.groups.year);

const replaced = 'hello world'.replace(/(\w+) (\w+)/u, '$2 $1');
```

`g` フラグを付けるとすべての一致を、付けないと最初の一致だけを返します。日本語などの非 ASCII 文字には `u` フラグが便利です。

Keywords: regex, regular expression, match, test, pattern, javascript, node.js, js.
