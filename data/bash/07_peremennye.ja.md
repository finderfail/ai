# Bash：変数

```bash
name="Ilya"            # = の前後に空白を入れない
echo "こんにちは、$name"
echo "${name}_backup"  # 波かっこで変数名を区切る
files=$(ls)            # コマンドの出力を代入
count=$((3 + 4))       # 算術演算
export PATH="$HOME/bin:$PATH"   # 子プロセスにも渡る環境変数
unset name             # 変数を削除
echo "${VAR:-default}" # VAR が空なら既定値
```

`name = "x"` のように空白を入れるとエラーになります（bash が `name` というコマンドを探すため）。`export` していない変数は、起動したプログラムからは見えません。
