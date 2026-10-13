# HTML5：アクセシビリティ（a11y）と ARIA

基本ルール：
- **正しい要素** を使う：ボタンは `<button>`、リンクは `<a href>`。`<div onclick>` にしない。
- 画像には `alt`、入力欄には `<label>`、ページには `lang`。
- 見出しは順番どおり、`<h1>` は1つ。
- すべてキーボードで操作でき、フォーカスが見える（`:focus-visible`）。
- 文字のコントラスト比は 4.5:1 以上。

ARIA は適切な HTML 要素がない場合だけ使う：
```html
<button aria-expanded="false" aria-controls="menu">メニュー</button>
<ul id="menu" hidden>…</ul>

<button aria-label="閉じる">×</button>
<div role="alert">保存エラー</div>
<div aria-live="polite">3件のファイルを読み込みました</div>
<span class="visually-hidden">スクリーンリーダー専用のテキスト</span>
<nav aria-label="パンくずリスト">…</nav>
<a href="#main" class="skip-link">本文へ移動</a>
```

ARIA の第一のルール：ネイティブ要素で済むなら ARIA を使わない。
