# Bash：アクセス権 chmod と chown

`ls -l` は `-rwxr-xr--` のように権限を表示します：所有者・グループ・その他。r は読み取り(4)、w は書き込み(2)、x は実行(1)です。

```bash
chmod +x script.sh        # 実行可能にする
chmod 644 file.txt        # rw-r--r-- ：通常のファイル
chmod 755 script.sh       # rwxr-xr-x ：スクリプトやディレクトリ
chmod 600 ~/.ssh/id_ed25519   # 秘密鍵：所有者のみ
chmod -R u+w dir/         # 所有者に書き込み権を再帰的に付与
sudo chown user:group file    # 所有者とグループを変更
```

`./script.sh` 実行時の `Permission denied` は、たいてい `x` 権限がないことが原因です。「とりあえず動かすため」に `chmod 777` にしないでください。誰でも書き込めるようになります。
