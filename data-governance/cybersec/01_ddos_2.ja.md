# DDoS 攻撃とその対策 — その2

## 対策

- CDN やトラフィック洗浄サービス（Cloudflare、Qrator、DDoS-Guard）が攻撃を受け止める。
- nginx やロードバランサーでのレート制限で、1つのアドレスからのリクエスト頻度を抑える。
- SYN cookies は半開き接続の状態を保持せずに SYN flood を防ぐ。
- キャッシュと CDN でオリジンの負荷を下げる。
- オートスケーリングでピークをしのげるが、インフラの請求額は増える。

nginx での制限の例：

```nginx
limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;

server {
    location /api/ {
        limit_req zone=api burst=20 nodelay;
    }
}
```

キーワード：DDoS、サービス妨害、フラッド、サイトへの攻撃。
