# Таймеры и отложенное выполнение

```javascript
const timer = setTimeout(() => console.log('через секунду'), 1000);
clearTimeout(timer);

const interval = setInterval(() => console.log('каждые 5 секунд'), 5000);
clearInterval(interval);

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function retry(fn, attempts = 3, delayMs = 500) {
  for (let i = 0; i < attempts; i += 1) {
    try {
      return await fn();
    } catch (error) {
      if (i === attempts - 1) throw error;
      await sleep(delayMs * (i + 1));
    }
  }
}
```

Незакрытый `setInterval` держит процесс Node.js запущенным. Для фоновых таймеров используют `timer.unref()`.

Keywords: timer, settimeout, setinterval, sleep, delay, retry, javascript, node.js, js.
