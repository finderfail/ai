# Пример HTML/CSS: группа кнопок

Сегментированная группа кнопок со скруглением по краям.

```html
<div class="btn-group" role="group" aria-label="View">
  <button aria-pressed="true">Day</button><button>Week</button><button>Month</button>
</div>
```

```css
.btn-group { display: inline-flex; border: 1px solid #d0d3da; border-radius: 10px; overflow: hidden; }
.btn-group button { padding: 8px 16px; border: 0; background: #fff; cursor: pointer; }
.btn-group button + button { border-left: 1px solid #d0d3da; }
.btn-group button[aria-pressed="true"] { background: #4f46e5; color: #fff; }
```
