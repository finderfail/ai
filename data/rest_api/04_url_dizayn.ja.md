# REST API：URL の設計

ルール：
- **複数形の名詞**：`/getUsers` ではなく `/users`、`/orders`。
- **パスに ID**：`/users/42`。
- **明確な所属関係なら入れ子** にするが、2階層まで：`/users/42/orders`。それ以上は独立したリソース：`/orders/987`。
- **フィルター、ソート、ページネーションはクエリで**：`/orders?status=paid&sort=-created_at&limit=20`。
- **小文字とハイフン**：`/payment-methods`。`.json` などの拡張子は付けない。
- **動詞を使わない**。CRUD に収まらない操作はサブリソースにする：`POST /orders/987/cancel` や `POST /orders/987/refunds`。
- **バージョン** はパスの先頭に：`/api/v1/...`。

例：
```
GET    /api/v1/users            一覧
POST   /api/v1/users            作成
GET    /api/v1/users/42         1件
PATCH  /api/v1/users/42         更新
DELETE /api/v1/users/42         削除
GET    /api/v1/users/42/orders  ユーザーの注文
```
