# OS 情報を返す /info エンドポイント付き HTTP サーバー — その2

```javascript
const http = require('http');
const os = require('os');

const HOST = '127.0.0.1';
const PORT = 3000;

function getSystemInfo() {
  const cpus = os.cpus();
  return {
    platform: os.platform(),
    release: os.release(),
    arch: os.arch(),
    hostname: os.hostname(),
    nodeVersion: process.version,
    cpuModel: cpus.length ? cpus[0].model : 'unknown',
    cpuCount: cpus.length,
    totalMemoryMb: Math.round(os.totalmem() / 1024 / 1024),
    freeMemoryMb: Math.round(os.freemem() / 1024 / 1024),
    uptimeSeconds: Math.round(os.uptime())
  };
}

const server = http.createServer((req, res) => {
  if (req.method === 'GET' && req.url === '/info') {
    res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
    res.end(JSON.stringify(getSystemInfo(), null, 2));
    return;
  }

  res.writeHead(404, { 'Content-Type': 'application/json; charset=utf-8' });
```
