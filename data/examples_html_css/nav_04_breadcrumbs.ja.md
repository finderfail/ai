# HTML/CSS の例: パンくずリスト

区切り記号と aria-current 付きのパンくず。

```html
<nav aria-label="Breadcrumb">
  <ol class="crumbs"><li><a href="/">Home</a></li><li><a href="/docs">Docs</a></li><li aria-current="page">CSS Grid</li></ol>
</nav>
```

```css
.crumbs { display: flex; flex-wrap: wrap; gap: 8px; list-style: none; padding: 0; font-size: 14px; }
.crumbs li + li::before { content: "/"; margin-right: 8px; color: #aaa; }
.crumbs a { color: #4f46e5; text-decoration: none; }
.crumbs [aria-current="page"] { color: #666; }
```
