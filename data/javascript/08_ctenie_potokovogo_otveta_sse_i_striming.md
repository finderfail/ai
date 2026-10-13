# Чтение потокового ответа (SSE и стриминг)

```javascript
const response = await fetch(url, { method: 'POST', body: JSON.stringify(payload) });
const reader = response.body.getReader();
const decoder = new TextDecoder();
let buffer = '';

while (true) {
  const { done, value } = await reader.read();
  if (done) break;
  buffer += decoder.decode(value, { stream: true });

  const parts = buffer.split('\n\n');
  buffer = parts.pop();
  for (const part of parts) {
    if (part.startsWith('data: ')) {
      const payload = JSON.parse(part.slice(6));
      process.stdout.write(payload.text || '');
    }
  }
}
```

Последний неполный фрагмент оставляют в буфере — иначе разорванный по границе пакета JSON не распарсится.

Keywords: stream, streaming, sse, server sent events, reader, javascript, node.js, js.
