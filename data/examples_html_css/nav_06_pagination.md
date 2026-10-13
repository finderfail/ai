# Пример HTML/CSS: пагинация

Номера страниц, активная страница и стрелки.

```html
<nav aria-label="Pagination">
  <ul class="pages">
    <li><a href="?p=1" aria-label="Previous">‹</a></li>
    <li><a href="?p=1">1</a></li><li><a href="?p=2" aria-current="page">2</a></li><li><a href="?p=3">3</a></li>
    <li><a href="?p=3" aria-label="Next">›</a></li>
  </ul>
</nav>
```

```css
.pages { display: flex; gap: 6px; list-style: none; padding: 0; }
.pages a { display: grid; place-items: center; min-width: 36px; height: 36px; padding: 0 8px;
  border-radius: 8px; border: 1px solid #ddd; color: #333; text-decoration: none; }
.pages a:hover { background: #f3f4f6; }
.pages a[aria-current="page"] { background: #4f46e5; border-color: #4f46e5; color: #fff; }
```
