# SQL インジェクションとその対策

ユーザーの入力がデータとしてではなく、SQL クエリのコードの一部として扱われると発生する脆弱性です。

脆弱なコード：

```python
query = f"SELECT * FROM users WHERE email = '{email}'"
cursor.execute(query)
```

入力 `' OR '1'='1` によって、条件がすべての行で真になります。

## 正しい方法：パラメータ化クエリ

```python
cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
```

ドライバーが値をエスケープするため、値が SQL として解釈されることはありません。

## 追加の対策

- ORM（SQLAlchemy、Django ORM）は既定でパラメータ化を使う。
- アプリケーションのアカウントは最小権限にする：DROP なし、他のスキーマへのアクセスなし。
- 入力形式（メール、数値、日付）の検証で攻撃面を減らす。
- SQL エラーの内容をユーザーに表示しない（攻撃者の手がかりになる）。

キーワード：SQL インジェクション、sql injection、データベースへの注入。
