# Git：タグとバージョン

```bash
git tag                         # タグ一覧
git tag v1.2.0                  # 現在のコミットに軽量タグ
git tag -a v1.2.0 -m "リリース 1.2.0"   # 注釈付きタグ（推奨）
git tag -a v1.1.0 abc1234 -m "..."     # 古いコミットにタグ
git push origin v1.2.0          # タグを1つ送信
git push --tags                 # すべてのタグを送信
git tag -d v1.2.0               # ローカルで削除
git push origin --delete v1.2.0 # サーバー上で削除
git switch --detach v1.2.0      # そのバージョンのコードを確認
```

`git push` は既定ではタグを送りません。バージョンにはセマンティックバージョニング（MAJOR.MINOR.PATCH）がよく使われます。
