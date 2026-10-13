# 外部への HTTP リクエスト：fetch

Node.js 18 以降は、ライブラリなしでグローバルな `fetch` が使えます。

```javascript
async function loadData(url) {
  const response = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query: 'test' })
  });

  if (!response.ok) {
    throw new Error(`HTTP ${response.status}`);
  }
  return response.json();
}
```

注意：`fetch` は 4xx や 5xx のコードでは例外を投げません。`response.ok` は自分で確認する必要があります。

Keywords: fetch, http request, api call, get post, javascript, node.js, js.
