# HTML5：グローバル属性と data 属性

グローバル属性（どの要素にも使える）：
- `id`、`class`、`style`、`title`、`lang`、`dir`；
- `hidden`：要素を隠す；
- `tabindex`：フォーカス順（`0` は通常の順、`-1` はプログラムからのみ）；
- `contenteditable`：編集可能なブロック；
- `draggable`：ドラッグ可能；
- `inert`：要素と子孫を無効にし、操作不能にする；
- `translate="no"`：翻訳しない；
- `spellcheck`、`autocapitalize`、`enterkeyhint`。

**data 属性**：JS や CSS 用の独自データ：
```html
<button class="buy" data-product-id="42" data-price="1990">購入</button>
<script>
  const btn = document.querySelector('.buy');
  btn.dataset.productId;   // "42"
  btn.dataset.price;       // "1990"
</script>
<style> [data-state="open"] { display: block; } </style>
```

`data-` の名前はハイフン区切り、`dataset` ではキャメルケース。値は常に文字列。
