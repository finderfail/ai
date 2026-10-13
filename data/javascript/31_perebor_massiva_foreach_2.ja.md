# 配列の反復：forEach とループ — その2

## その他の方法

```javascript
for (let i = 0; i < users.length; i++) {
  console.log(users[i]);
}

const upper = users.map((name) => name.toUpperCase());

for (const key in { a: 1, b: 2 }) {
  console.log(key);
}
```

`for...in` は配列の値ではなく**オブジェクトのキー**を反復するので、配列には使いません。`map` は新しい配列を返しますが、`forEach` は返しません。

## forEach と async

`forEach` は非同期のコールバックを待ちません：

```javascript
for (const name of users) {
  await save(name);
}

await Promise.all(users.map((name) => save(name)));
```

1つ目は順番に、2つ目は並列に実行します。`users.forEach(async ...)` は完了を待ちません。

Keywords: forEach, for of, for in, loop, iterate, array iteration, 配列の反復, ループ.
