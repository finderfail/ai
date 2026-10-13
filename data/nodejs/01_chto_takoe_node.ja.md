# Node.js：何か、どう動くか

**Node.js** はブラウザの外で JavaScript を動かす実行環境で、次から成ります：
- **V8**：Google の JavaScript エンジン（Chrome と同じ）。JS を機械語にコンパイルする；
- **libuv**：イベントループ、非同期 I/O、スレッドプール（ファイル、DNS、crypto、zlib）を提供する C ライブラリ；
- **標準ライブラリ**：`node:fs`、`node:http`、`node:path`、`node:crypto`、`node:stream`、`node:events` など。

中心となる考え方は **JavaScript は1スレッド＋ノンブロッキング I/O**。データベースやネットワークの応答を待つ間に、他のリクエストを処理する。そのため I/O 中心の処理（API、プロキシ、チャット、ストリーミング）に向くが、メインスレッドでの重い計算は全員を止めてしまう。

Node には `window` や DOM はなく、グローバルオブジェクトは `globalThis`（`global` と同じ）。`process`、`Buffer`、`fetch`（Node 18 以降）、`setTimeout`、`structuredClone`、`URL`、`AbortController` がある。

バージョン：偶数のメジャーバージョンが LTS（長期サポート）になる。本番では最新の LTS を選ぶ（nodejs.org で確認）。
