# Исходящие HTTP-запросы: fetch

Начиная с Node.js 18 глобальный `fetch` доступен без установки библиотек.

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

Важно: `fetch` не бросает исключение на коды 4xx и 5xx — проверять `response.ok` нужно самостоятельно.

Keywords: fetch, http request, api call, get post, javascript, node.js, js.
