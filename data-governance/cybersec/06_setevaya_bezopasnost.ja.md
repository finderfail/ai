# ネットワークセキュリティ

## 基本原則

- 外部に不要なものはすべて閉じる：データベース、キャッシュ、管理画面は localhost か内部ネットワークだけで待ち受ける。
- ファイアウォールは「明示的に許可したもの以外はすべて拒否」で運用する。
- SSH は鍵認証のみとし、root ログインとパスワード認証を無効にする。

ufw の設定例：

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

`/etc/ssh/sshd_config` の SSH 設定：

```
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
```

## セグメンテーション

ネットワークをゾーンに分けると攻撃の拡大を抑えられます。Web サーバーから他サービスのデータベースへ直接アクセスできないように、作業端末から本番環境へ直接アクセスできないようにします。

キーワード：ネットワークセキュリティ、ファイアウォール、firewall、ufw、SSH、ポート。
