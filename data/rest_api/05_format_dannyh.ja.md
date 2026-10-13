# REST API：リクエストとレスポンスの形式

- 形式は **JSON**、`Content-Type: application/json; charset=utf-8`。
- フィールド名は API 全体で1つのスタイルに統一：`camelCase` か `snake_case`。
- 日付は UTC の **ISO 8601** 文字列：`"2026-10-12T14:30:00Z"`。
- 金額は最小単位の整数（`amountMinor: 1999`）か10進数の文字列にし、ISO 4217 の通貨コード（`"currency": "JPY"`）を添える。金額に float は使わない。
- ID は文字列（UUID、ULID）か数値のどちらかに統一。
- `null` は値が明示的にないことを表す。フィールド自体の欠落とは混ぜないほうがよい。
- 列挙値は文字列で：`"status": "paid"`。

一覧のレスポンス：
```json
{
  "data": [{ "id": "u_1", "email": "a@example.com" }],
  "meta": { "total": 134, "limit": 20, "nextCursor": "eyJpZCI6MjB9" }
}
```

単一のリソースはオブジェクトのままでも `{ "data": {...} }` でもよいが、API 全体で統一すること。
