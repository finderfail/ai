# REST API：キャッシュと条件付きリクエスト

ヘッダー：
- `Cache-Control: no-store`：個人的なデータや機密データ。
- `Cache-Control: public, max-age=300`：公開データは5分キャッシュ可能。
- `Cache-Control: private, max-age=60`：ユーザーのブラウザ内だけでキャッシュ。

**ETag と条件付きリクエスト**：
```
GET /products/42
200 OK
ETag: "v17"

GET /products/42
If-None-Match: "v17"
304 Not Modified
```
リソースが変わっていなければサーバーは本文を返さず、通信量を節約できる。

**楽観的ロック**：更新時にクライアントが `If-Match: "v17"` を送る。すでに変更されていれば、サーバーは **412 Precondition Failed** を返し、他人の変更を上書きしない。

`Last-Modified` / `If-Modified-Since` も同様に動くが、精度は秒単位。
