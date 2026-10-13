# Bash：スクリプトの書き方と実行

```bash
#!/usr/bin/env bash
set -euo pipefail

main() {
  echo "引数: $*"
}

main "$@"
```

実行：`chmod +x script.sh && ./script.sh 引数1 引数2` または `bash script.sh`。

`set -e` は最初のエラーで終了、`-u` は未定義変数の参照をエラーに、`-o pipefail` はパイプのどこかの失敗をエラーにします。気づかない失敗を防げます。

スクリプトの引数：`$0` は名前、`$1..$9` は位置引数、`"$@"` はすべて（個別に）、`$#` は個数。終了コードは `exit N` で指定します。
