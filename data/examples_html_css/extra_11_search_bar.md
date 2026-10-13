# Пример HTML/CSS: поле поиска с иконкой

Поиск с иконкой внутри и очисткой.

```html
<label class="search"><span aria-hidden="true">🔍</span><input type="search" placeholder="Search…" aria-label="Search"></label>
```

```css
.search { display: flex; align-items: center; gap: 8px; padding: 0 14px; border: 1px solid #d1d5db; border-radius: 999px; }
.search:focus-within { border-color: #4f46e5; box-shadow: 0 0 0 3px #e0e7ff; }
.search input { flex: 1; border: 0; outline: 0; padding: 10px 0; background: transparent; }
```
