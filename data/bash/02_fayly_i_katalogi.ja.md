# Bash：作成・コピー・移動・削除

```bash
mkdir -p a/b/c          # 入れ子のディレクトリを作成
touch file.txt          # 空ファイル作成／更新時刻の更新
cp src.txt dst.txt      # ファイルをコピー
cp -r dir/ backup/      # ディレクトリを再帰的にコピー
mv old.txt new.txt      # 名前変更または移動
rm file.txt             # ファイル削除
rm -r dir/              # ディレクトリごと削除
rmdir empty_dir         # 空のディレクトリを削除
```

`rm` はゴミ箱を経由せず完全に削除します。`rm -rf` の前にはパスと変数を必ず確認してください。`$DIR` が空だと `rm -rf "$DIR"/` は `rm -rf /` になります。1件ずつ確認するには `rm -ri` を使います。
