# HTML5: мета-теги, SEO и превью ссылок

```html
<title>Купить кроссовки — Shop</title>
<meta name="description" content="Описание страницы 140–160 символов">
<link rel="canonical" href="https://example.com/shoes">
<meta name="robots" content="index, follow">

<meta property="og:title" content="Кроссовки">
<meta property="og:description" content="Новая коллекция">
<meta property="og:image" content="https://example.com/og.jpg">
<meta property="og:url" content="https://example.com/shoes">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">

<link rel="alternate" hreflang="ja" href="https://example.com/ja/shoes">

<script type="application/ld+json">
{"@context": "https://schema.org", "@type": "Organization", "name": "Shop", "url": "https://example.com"}
</script>
```

- Уникальные `title` и `description` для каждой страницы.
- Open Graph отвечает за превью ссылок в мессенджерах и соцсетях.
