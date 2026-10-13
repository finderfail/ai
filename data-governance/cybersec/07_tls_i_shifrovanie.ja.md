# TLS と通信の暗号化

TLS はクライアントとサーバー間のデータを暗号化し、証明書でサーバーの正当性を確認します。

## 実践

- TLS 1.2 と 1.3 だけを使い、SSLv3、TLS 1.0、1.1 は無効にする。
- 証明書は Let's Encrypt で発行し、certbot で自動更新する。
- HSTS を有効にし、ブラウザが暗号化なしの接続を試みないようにする。
- HTTP のトラフィックはすべて HTTPS にリダイレクトする。

```nginx
server {
    listen 443 ssl http2;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers off;
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
}

server {
    listen 80;
    return 301 https://$host$request_uri;
}
```

共通鍵暗号（AES）は高速でデータ本体に、公開鍵暗号（RSA、ECDSA）は鍵交換と署名に使います。TLS は両方を組み合わせ、公開鍵暗号でセッション鍵を合意した後は共通鍵暗号で通信します。

キーワード：TLS、SSL、HTTPS、証明書、通信の暗号化。
