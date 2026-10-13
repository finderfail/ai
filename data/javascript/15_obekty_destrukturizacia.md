# Объекты и деструктуризация

```javascript
const config = { host: '127.0.0.1', port: 3000, debug: false };

const { host, port, timeout = 5000 } = config;
const { debug: isDebug } = config;

const merged = { ...config, port: 8080 };
const { port: _removed, ...withoutPort } = config;

const keys = Object.keys(config);
const entries = Object.entries(config);
const restored = Object.fromEntries(entries);
```

Значение по умолчанию (`timeout = 5000`) применяется только если свойство равно `undefined`, но не если оно `null` или `0`.

Keywords: object, destructuring, spread, keys, entries, javascript, node.js, js.
