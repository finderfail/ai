# Bash：パイプ

記号 `|` は、あるコマンドの出力を次のコマンドの入力に渡します。

```bash
ls -l | wc -l                          # ls の出力行数
cat access.log | grep 500 | wc -l      # 500 を含む行数
ps aux | grep python                   # python のプロセスを探す
history | tail -20                     # 直近20件のコマンド
sort names.txt | uniq -c | sort -rn    # 行の出現回数を多い順に
```

`uniq` は隣接する重複しか消さないため、前にはほぼ必ず `sort` が必要です。

パイプ全体の終了コードは、既定では最後のコマンドのものです。`set -o pipefail` を使うと、途中のどれかが失敗した場合にパイプ全体が失敗扱いになります。
