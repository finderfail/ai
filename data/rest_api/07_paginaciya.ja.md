# REST API：ページネーション、フィルター、ソート

**オフセット方式**：`GET /orders?limit=20&offset=40`
- 単純で、任意のページに移動できる。
- 大きなテーブルでは遅く、途中で挿入があるとページ間で行がずれる。

**カーソル方式**：`GET /orders?limit=20&cursor=eyJpZCI6...`
- サーバーが `nextCursor`（最後のソートキーをエンコードしたもの）を返す。
- 挿入があっても安定し、高速（`WHERE id > :last ORDER BY id LIMIT 20`）。
- 任意のページには移動できない。

推奨：
- `limit` を制限する（既定20、最大100）。
- メタデータを返す：`nextCursor`、`hasMore`、必要なら `total`。
- `rel="next"` 付きの `Link` ヘッダーを加えてもよい。

**フィルター**：`?status=paid&createdFrom=2026-01-01`
**ソート**：`?sort=-createdAt,amount`（マイナスは降順）
**フィールド選択**：`?fields=id,email`
ソートやフィルターはインデックスのあるフィールドだけに許可する。
