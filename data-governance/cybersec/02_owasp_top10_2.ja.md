# OWASP Top 10：Web アプリケーションの主なリスク — その2

1. **Broken Access Control**（アクセス制御の不備）：他人のデータや管理機能にアクセスできてしまう。
2. **Cryptographic Failures**（暗号化の失敗）：データが適切に暗号化されずに送信・保存される。
3. **Injection**（インジェクション）：SQL インジェクション、コマンドインジェクション、LDAP。
4. **Insecure Design**（安全でない設計）：パッチでは直せない設計上の誤り。
5. **Security Misconfiguration**（セキュリティ設定ミス）：初期パスワード、公開された管理画面、本番での詳細なエラー表示。
6. **Vulnerable and Outdated Components**：既知の脆弱性がある古いライブラリ。
7. **Identification and Authentication Failures**：弱いパスワード、総当たり対策の欠如。
8. **Software and Data Integrity Failures**：署名を検証しない更新や依存関係。
9. **Security Logging and Monitoring Failures**：攻撃に気づけず調査もできない。
10. **Server-Side Request Forgery（SSRF）**：サーバーに内部リソースへアクセスさせる。
