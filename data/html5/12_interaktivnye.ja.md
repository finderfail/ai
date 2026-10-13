# HTML5：JavaScript なしのインタラクティブ要素

```html
<details>
  <summary>プランを変更するには？</summary>
  <p>アカウント設定を開いて…</p>
</details>

<dialog id="dlg">
  <form method="dialog">
    <p>ファイルを削除しますか？</p>
    <button value="cancel">キャンセル</button>
    <button value="ok">削除</button>
  </form>
</dialog>
<button onclick="dlg.showModal()">ダイアログを開く</button>

<button popovertarget="tip">ヒント</button>
<div id="tip" popover>ポップアップの文章</div>

<template id="row">
  <li class="item"></li>
</template>

<progress value="70" max="100">70%</progress>
<meter value="0.6" min="0" max="1">60%</meter>
```

- `<details>`：開閉できるブロック（FAQ、ネタバレ防止）。
- `showModal()` 付きの `<dialog>`：背景を暗くし、Esc で閉じるモーダル。
- `popover`：JS なしのポップアップ（新しいブラウザ）。
- `<template>`：JavaScript で複製するためのマークアップ。
