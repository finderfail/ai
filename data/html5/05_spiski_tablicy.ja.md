# HTML5：リストと表

```html
<ul><li>箇条書き</li></ul>
<ol start="3" reversed><li>番号付き</li></ol>
<dl><dt>用語</dt><dd>説明</dd></dl>

<table>
  <caption>四半期別の売上</caption>
  <thead>
    <tr><th scope="col">四半期</th><th scope="col">金額</th></tr>
  </thead>
  <tbody>
    <tr><th scope="row">Q1</th><td>120 000</td></tr>
    <tr><th scope="row">Q2</th><td>150 000</td></tr>
  </tbody>
  <tfoot>
    <tr><th scope="row">合計</th><td>270 000</td></tr>
  </tfoot>
</table>
```

- 表は表形式のデータだけに使い、ページのレイアウトには使わない。
- `<th scope>` と `<caption>` はスクリーンリーダーを助ける。
- セルの結合：`colspan="2"`、`rowspan="3"`。
- 幅の広い表は、スマホ向けに `overflow-x: auto` のコンテナで囲む。
