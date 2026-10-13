# Bash：配列と文字列操作

```bash
arr=(one two three)
echo "${arr[0]}"        # 最初の要素
echo "${arr[@]}"        # すべての要素
echo "${#arr[@]}"       # 配列の長さ
arr+=(four)             # 追加
for x in "${arr[@]}"; do echo "$x"; done

s="hello world"
echo "${#s}"            # 文字列の長さ
echo "${s:0:5}"         # 部分文字列：hello
echo "${s/world/bash}"  # 最初の一致を置換
file="photo.jpg"
echo "${file%.jpg}"     # 接尾辞を除去：photo
echo "${file##*.}"      # 拡張子：jpg
```

`"${arr[@]}"` を引用符で囲むと、空白を含む要素も別々の要素として扱われます。
