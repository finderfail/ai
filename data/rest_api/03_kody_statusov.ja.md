# REST API：HTTP ステータスコード

**2xx：成功**
- 200 OK：GET、PUT、PATCH の成功。
- 201 Created：リソース作成（POST）。`Location` ヘッダーでその場所を示す。
- 202 Accepted：非同期処理として受け付けた。
- 204 No Content：本文なしの成功（DELETE に多い）。

**3xx：リダイレクト**
- 301/308：恒久的、302/307：一時的、304 Not Modified：キャッシュが有効。

**4xx：クライアントエラー**
- 400 Bad Request：不正なリクエストや無効なデータ。
- 401 Unauthorized：未認証、またはトークンが無効。
- 403 Forbidden：認証済みだが権限がない。
- 404 Not Found：リソースが存在しない。
- 405 Method Not Allowed：その URL でそのメソッドは使えない。
- 409 Conflict：状態の競合（重複、バージョン）。
- 415 Unsupported Media Type：Content-Type が不正。
- 422 Unprocessable Content：構文は正しいが業務上の検証に通らない。
- 429 Too Many Requests：上限超過。`Retry-After` を参照。

**5xx：サーバーエラー**
- 500 Internal Server Error、502 Bad Gateway、503 Service Unavailable、504 Gateway Timeout。
