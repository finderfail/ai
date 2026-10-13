# os モジュール：OS の情報

`os` は標準モジュールで、プロセスが動いているホストの情報を取得できます。

```javascript
const os = require('os');

const info = {
  platform: os.platform(),
  release: os.release(),
  arch: os.arch(),
  hostname: os.hostname(),
  cpus: os.cpus().length,
  cpuModel: os.cpus()[0].model,
  totalMemory: os.totalmem(),
  freeMemory: os.freemem(),
  uptime: os.uptime()
};
```

便利な値：`os.platform()` は `linux`、`darwin`、`win32` を返す。`os.arch()` は `x64`、`arm64`。`os.totalmem()` と `os.freemem()` はバイト単位。`os.uptime()` は起動からの秒数。`os.cpus()` はコアの配列で、長さが論理プロセッサ数です。

グローバルな `process` からは `process.platform`、`process.arch`、`process.version`（Node.js のバージョン）、`process.pid`、`process.memoryUsage()` が使えます。

Keywords: os module, system info, platform, cpu, memory, hostname, uptime, javascript, node.js, js.
