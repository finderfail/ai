# 配列の反復：forEach とループ — その1

`forEach` は配列の各要素に対して関数を呼び出します。戻り値はありません。

```javascript
const users = ['Aiko', 'Kenji', 'Yui'];

users.forEach((name) => {
  console.log(name);
});

users.forEach((name, index, array) => {
  console.log(`${index + 1} / ${array.length}: ${name}`);
});
```

コールバックは要素、インデックス、配列自体の3つの引数を受け取ります。

## forEach の中では break を書けない

`forEach` 内の `break` や `continue` は構文エラーで、コードは動きません。コールバック内の `return` は現在の反復を終えるだけで、ループは止まりません。次のコードは誤りです：

```javascript
users.forEach((name) => {
  if (name === 'Kenji') break;
});
```

## break が必要なら for...of

途中で抜けたい場合は `for...of` を使います。正しい書き方：

```javascript
for (const name of users) {
  if (name === 'Kenji') break;
  console.log(name);
}

for (const [index, name] of users.entries()) {
  console.log(index, name);
}
```
