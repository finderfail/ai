# タイマーと遅延実行

```javascript
const timer = setTimeout(() => console.log('1秒後'), 1000);
clearTimeout(timer);

const interval = setInterval(() => console.log('5秒ごと'), 5000);
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

止めていない `setInterval` は Node.js のプロセスを終了させません。バックグラウンドのタイマーには `timer.unref()` を使います。

Keywords: timer, settimeout, setinterval, sleep, delay, retry, javascript, node.js, js.
