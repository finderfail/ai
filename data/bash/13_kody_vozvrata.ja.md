# Bash：終了コードとエラー処理

コマンドは必ず終了コードを返します：`0` は成功、それ以外はエラー。直前のコマンドのコードは `$?` に入ります。

```bash
grep -q "error" log.txt
echo $?                      # 0：見つかった、1：見つからない

mkdir build && cd build      # mkdir が成功したときだけ cd
cd /nope || exit 1           # cd に失敗したら終了

if ! command -v git >/dev/null; then
  echo "git がインストールされていません" >&2
  exit 1
fi

trap 'echo "エラー: $LINENO 行目" >&2' ERR
trap 'rm -f "$tmp"' EXIT     # 終了時に後片付け
```

エラーメッセージは標準エラーに出します：`echo "..." >&2`。
