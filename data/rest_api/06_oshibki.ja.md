# REST API：エラーの形式（RFC 9457）

**Problem Details for HTTP APIs**（RFC 9457、RFC 7807 を置き換え）は、`application/problem+json` 型の統一的なエラー形式を定めています：

```json
{
  "type": "https://api.example.com/problems/validation",
  "title": "Validation failed",
  "status": 400,
  "detail": "email フィールドの形式が正しくありません",
  "instance": "/api/v1/users",
  "errors": [
    { "field": "email", "message": "メールアドレスの形式が不正です" }
  ]
}
```

- `type`：エラーの種類を識別する URI（ドキュメントへのリンクでもよい）。
- `title`：エラーの種類の短い説明、`detail`：その事例の具体的な説明。
- `status`：HTTP コードと同じ値。
- 追加のフィールド（`errors`、`traceId`）も使える。

ルール：すべてのエラーで同じ形式、クライアント開発者に分かるメッセージ、機械可読なコード、5xx ではスタックや内部情報を出さない、ログ検索用の `traceId`。
