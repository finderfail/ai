# Пример HTML/CSS: строка поиска

Поле поиска с иконкой внутри.

```html
<form class="search" role="search">
  <input type="search" placeholder="Search…" aria-label="Search">
</form>
```

```css
.search input {
  width: 100%; max-width: 420px; padding: 12px 16px 12px 42px;
  border: 1px solid #d0d3da; border-radius: 999px; font: inherit;
  background: #fff url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='18' height='18' fill='none' stroke='%23888' stroke-width='2'%3E%3Ccircle cx='8' cy='8' r='6'/%3E%3Cpath d='M13 13l4 4'/%3E%3C/svg%3E") no-repeat 16px center;
}
```
