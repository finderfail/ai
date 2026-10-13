# ストリーミング応答の読み取り（SSE とストリーミング）

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

最後の不完全な断片はバッファに残します。そうしないと、パケットの境界で切れた JSON を解析できません。

Keywords: stream, streaming, sse, server sent events, reader, javascript, node.js, js.
