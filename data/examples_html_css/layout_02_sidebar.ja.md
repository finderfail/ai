# HTML/CSS の例: サイドバーと本文

固定幅のサイドバーと伸縮するメイン部分。

```html
<div class="layout"><aside class="sidebar">Menu</aside><main class="content">Content</main></div>
```

```css
.layout { display: flex; min-height: 100vh; }
.sidebar { flex: 0 0 260px; padding: 16px; background: #f5f5f7; }
.content { flex: 1; min-width: 0; padding: 24px; }
@media (max-width: 700px) { .layout { flex-direction: column; } .sidebar { flex-basis: auto; } }
```
