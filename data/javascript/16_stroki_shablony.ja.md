# 文字列とテンプレートリテラル

```javascript
const name = '世界';
const greeting = `こんにちは、${name}！`;
const multiline = `1行目
2行目`;

'abc'.padStart(5, '0');
'  テキスト  '.trim();
'a,b,c'.split(',');
['a', 'b'].join('-');
'HELLO'.toLowerCase();
'text'.replaceAll('t', 'T');
'abcdef'.slice(1, 3);
'abc'.includes('b');
```

`replaceAll` は Node.js 15 以降が必要です。それより古い版では、正規表現と `g` フラグを付けた `replace` を使います。

Keywords: string, template literal, split, join, trim, replace, javascript, node.js, js.
