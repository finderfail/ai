# 非同期処理：Promise と async/await

```javascript
async function main() {
  try {
    const [users, posts] = await Promise.all([
      fetch('/api/users').then((r) => r.json()),
      fetch('/api/posts').then((r) => r.json())
    ]);
    console.log(users.length, posts.length);
  } catch (error) {
    console.error('エラー:', error.message);
  }
}
```

`Promise.all` はリクエストを並列に実行し、1つでも失敗すると全体が失敗します。`Promise.allSettled` は、拒否されたものも含めてすべての結果を返します。

Keywords: async, await, promise, promises, asynchronous, javascript, node.js, js.
