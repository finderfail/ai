# REST API：OpenAPI によるドキュメント

**OpenAPI**（旧 Swagger）は、HTTP API を YAML か JSON で記述する、機械可読な標準形式。現在の仕様のバージョンは 3.0 と 3.1。

```yaml
openapi: 3.1.0
info:
  title: Shop API
  version: 1.0.0
paths:
  /users/{id}:
    get:
      summary: ユーザーを取得
      parameters:
        - name: id
          in: path
          required: true
          schema: { type: string }
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema: { $ref: '#/components/schemas/User' }
        '404': { description: Not found }
components:
  schemas:
    User:
      type: object
      required: [id, email]
      properties:
        id: { type: string }
        email: { type: string, format: email }
```

利点：対話型ドキュメント（Swagger UI、Redoc）、クライアントやサーバースタブの生成、リクエストの検証、契約テスト。仕様はコードと同じリポジトリで管理する。
