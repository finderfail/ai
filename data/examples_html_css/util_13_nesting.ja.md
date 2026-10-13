# HTML/CSS の例: CSS ネスト

プリプロセッサなしのネイティブなネスト。

```html
<nav class="menu"><a href="#">Home</a></nav>
```

```css
.menu {
  display: flex; gap: 12px;
  & a { color: #374151; text-decoration: none;
    &:hover { color: #4f46e5; }
  }
  @media (max-width: 600px) { flex-direction: column; }
}
```
