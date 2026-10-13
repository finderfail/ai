# Bash：ネットワーク — curl・ssh・scp

```bash
curl https://example.com                  # GET して画面に表示
curl -o page.html https://example.com     # ファイルに保存
curl -L URL                               # リダイレクトに従う
curl -I URL                               # ヘッダーのみ
curl -X POST -H "Content-Type: application/json" \
     -d '{"name":"test"}' https://api.example.com/items
curl -fsS URL                             # 静かに、ただしエラーは表示

ssh user@host                             # 接続
ssh -i ~/.ssh/key user@host               # 鍵を指定
scp file.txt user@host:/tmp/              # サーバーへコピー
scp user@host:/var/log/app.log .          # サーバーからコピー
rsync -avz dir/ user@host:/backup/dir/    # 同期
ssh-keygen -t ed25519                     # 鍵を作成
```
