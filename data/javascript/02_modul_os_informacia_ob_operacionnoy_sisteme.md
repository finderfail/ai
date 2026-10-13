# Модуль os: информация об операционной системе

Модуль `os` — стандартный, даёт данные о хосте, на котором запущен процесс.

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

Полезные поля: `os.platform()` возвращает `linux`, `darwin`, `win32`; `os.arch()` — `x64`, `arm64`; `os.totalmem()` и `os.freemem()` возвращают байты; `os.uptime()` — секунды с момента загрузки; `os.cpus()` — массив ядер, его длина равна числу логических процессоров.

Из глобального объекта `process` доступны: `process.platform`, `process.arch`, `process.version` (версия Node.js), `process.pid`, `process.memoryUsage()`.

Keywords: os module, system info, platform, cpu, memory, hostname, uptime, javascript, node.js, js.
