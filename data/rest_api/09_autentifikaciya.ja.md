# REST API：認証と認可

方式：
- **API キー**：`Authorization: Bearer <key>` か `X-API-Key` ヘッダー。シンプルで、サーバー間通信やプラグインに向く。キーはハッシュだけを保存し、名前を付け、取り消せるようにする。
- **Bearer トークン（JWT）**：有効期限の短い署名付きトークン。リフレッシュトークンで更新する。
- **OAuth 2.0**：第三者アプリへのアクセス委譲。ユーザーがいるアプリには Authorization Code + PKCE、サービス間には Client Credentials。
- **cookie セッション**：同じドメインの自社 Web フロントエンド向け（`HttpOnly`、`Secure`、`SameSite`）。

ルール：
- HTTPS のみ。秘密情報を URL に入れない（ログに残る）。
- 401 は認証情報がないか不正、403 は権限なし。
- 認可はリクエストごと、オブジェクト単位で確認する：ユーザー A がユーザー B の `/orders/{id}` を読めてはいけない（BOLA/IDOR、OWASP API Top 10 の第1位）。
- 最小権限の原則：範囲（スコープ）を限定したキー。
