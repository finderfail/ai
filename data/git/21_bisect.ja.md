# Git：バグを入れたコミットを探す — bisect

`git bisect` は二分探索で、エラーが発生し始めたコミットを見つけます。

```bash
git bisect start
git bisect bad                # 現在のバージョンは壊れている
git bisect good v1.4.0        # このバージョンは正常だった
# git が中間のコミットに切り替えるので、確認して印を付ける：
git bisect good               # または git bisect bad
# … git が原因のコミットを示すまで繰り返す
git bisect reset              # 元に戻る
```

自動化：`git bisect run ./test.sh` — スクリプトは正常なら 0、エラーがあれば 0 以外を返すようにします。
