# Bash：プロセスとジョブ

```bash
ps aux | grep node       # プロセスを探す
pgrep -fl node           # 同じことを短く
top                      # リアルタイムの負荷（htop の方が便利）
kill 1234                # 終了を要求（SIGTERM）
kill -9 1234             # 強制終了（SIGKILL）、最後の手段
pkill -f "python app.py" # 名前やコマンドラインで終了
lsof -i :8000            # ポート8000を使っているプロセス

long_task &              # バックグラウンドで実行
jobs                     # 現在のシェルのジョブ一覧
fg %1                    # ジョブをフォアグラウンドに戻す
nohup ./server.sh > out.log 2>&1 &   # ターミナルを閉じても終了しない
```

Ctrl+C で中断、Ctrl+Z で一時停止（その後 `bg` か `fg`）。
