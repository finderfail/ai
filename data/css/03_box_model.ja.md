# CSS：ボックスモデル

各要素は層の重なった四角形：**content → padding → border → margin**。

```css
.card {
  width: 300px;
  padding: 16px;              /* 内側の余白 */
  border: 1px solid #ddd;
  margin: 24px auto;          /* 外側の余白。左右 auto でブロックを中央寄せ */
}

*, *::before, *::after {
  box-sizing: border-box;
}
```

- 既定は `box-sizing: content-box` で、`width` は内容だけの幅。全体の幅は 300 + 2·16 + 2·1 = 334px になる。
- `box-sizing: border-box` では `width` に padding と border を含み、ちょうど 300px になる。通常すべての要素に指定する。
- **マージンの相殺**：隣り合うブロックの上下マージンは足されず、大きいほうが使われる。flex/grid コンテナ内では起きない。
- 省略形：`margin: 10px 20px`（上下、左右）、`margin: 1px 2px 3px 4px`（上から時計回り）。
- `display: block` は幅いっぱい、`inline` は内容の幅で width/height なし、`inline-block` は行内だがサイズを持てる。
