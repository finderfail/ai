# HTML5：メタタグ、SEO、リンクのプレビュー

```html
<title>スニーカーを買う — Shop</title>
<meta name="description" content="120〜160文字程度のページの説明">
<link rel="canonical" href="https://example.com/shoes">
<meta name="robots" content="index, follow">

<meta property="og:title" content="スニーカー">
<meta property="og:description" content="新コレクション">
<meta property="og:image" content="https://example.com/og.jpg">
<meta property="og:url" content="https://example.com/shoes">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">

<link rel="alternate" hreflang="ru" href="https://example.com/ru/shoes">
<meta name="theme-color" content="#7b5cff">
<link rel="manifest" href="/manifest.json">

<script type="application/ld+json">
{"@context": "https://schema.org", "@type": "Organization", "name": "Shop", "url": "https://example.com"}
</script>
```

- ページごとに固有の `title` と `description` を付ける。
- Open Graph はメッセンジャーや SNS でのリンクのプレビューを決める。
