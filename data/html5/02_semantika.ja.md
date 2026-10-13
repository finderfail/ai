# HTML5：セマンティック要素

```html
<header>
  <nav aria-label="メインメニュー">
    <ul><li><a href="/">ホーム</a></li><li><a href="/blog">ブログ</a></li></ul>
  </nav>
</header>
<main>
  <article>
    <h1>記事の見出し</h1>
    <p>本文…</p>
    <section>
      <h2>セクション</h2>
      <figure>
        <img src="chart.png" alt="1年間の売上の伸び">
        <figcaption>図1 売上</figcaption>
      </figure>
    </section>
  </article>
  <aside>関連記事</aside>
</main>
<footer><small>© 2026</small></footer>
```

- `<main>`：主要な内容。ページに1つ。
- `<article>`：独立したコンテンツ（投稿、商品カード）。
- `<section>`：見出しを持つテーマ別の区分。
- `<aside>`：補足的な内容、`<nav>`：ナビゲーション。
- `<div>` と `<span>` は意味を持たない装飾用。

セマンティクスはスクリーンリーダーや検索エンジンを助け、CSS も書きやすくなる。
