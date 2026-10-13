# Node.js：worker_threads、child_process、cluster

**worker_threads**：重い計算（ハッシュ、パース、圧縮）用の本物のスレッドで、イベントループを止めない：
```javascript
const { Worker } = require('node:worker_threads');
const worker = new Worker('./heavy.js', { workerData: { n: 40 } });
worker.on('message', (result) => console.log(result));
```
`heavy.js` の中：`const { parentPort, workerData } = require('node:worker_threads'); parentPort.postMessage(fib(workerData.n));`

**child_process**：外部プログラムの実行：
```javascript
const { execFile, spawn } = require('node:child_process');
execFile('git', ['log', '--oneline', '-5'], (err, stdout) => console.log(stdout));
const proc = spawn('ffmpeg', ['-i', 'in.mp4', 'out.webm']);
```
引数を配列で渡す `execFile`/`spawn` を使う。ユーザー入力から組み立てた文字列を `exec` に渡すとコマンドインジェクションの危険がある。

**cluster**：1つのポートで複数の Node プロセスを動かし、全コアを使う。現在はロードバランサーの背後で Docker、systemd、PM2 により複数インスタンスを起動することが多い。
