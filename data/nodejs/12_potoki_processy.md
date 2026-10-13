# Node.js: worker_threads, child_process, cluster

**worker_threads** — настоящие потоки для тяжёлых вычислений (хеширование, парсинг, сжатие), не блокирующие цикл событий:
```javascript
const { Worker } = require('node:worker_threads');
const worker = new Worker('./heavy.js', { workerData: { n: 40 } });
worker.on('message', (result) => console.log(result));
```
В `heavy.js`: `const { parentPort, workerData } = require('node:worker_threads'); parentPort.postMessage(fib(workerData.n));`

**child_process** — запуск внешних программ:
```javascript
const { execFile, spawn } = require('node:child_process');
execFile('git', ['log', '--oneline', '-5'], (err, stdout) => console.log(stdout));
const proc = spawn('ffmpeg', ['-i', 'in.mp4', 'out.webm']);
```
Передавайте аргументы массивом: `exec` со строкой из пользовательского ввода — инъекция команд.

**cluster** — несколько процессов на одном порту; сейчас чаще несколько экземпляров через Docker или PM2.
