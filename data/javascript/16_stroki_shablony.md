# Строки и шаблонные литералы

```javascript
const name = 'мир';
const greeting = `Привет, ${name}!`;
const multiline = `первая строка
вторая строка`;

'abc'.padStart(5, '0');
'  текст  '.trim();
'a,b,c'.split(',');
['a', 'b'].join('-');
'Привет'.toLowerCase();
'text'.replaceAll('t', 'T');
'abcdef'.slice(1, 3);
'abc'.includes('b');
```

`replaceAll` требует Node.js 15+. В более старых версиях используют `replace` с регулярным выражением и флагом `g`.

Keywords: string, template literal, split, join, trim, replace, javascript, node.js, js.
