# Пример HTML/CSS: мобильное меню без JS

Бургер-меню на скрытом чекбоксе.

```html
<nav class="nav">
  <input type="checkbox" id="menu-toggle" hidden>
  <label for="menu-toggle" class="burger" aria-label="Menu">☰</label>
  <ul class="menu"><li><a href="#">Home</a></li><li><a href="#">Blog</a></li><li><a href="#">Contact</a></li></ul>
</nav>
```

```css
.menu { display: flex; gap: 20px; list-style: none; margin: 0; padding: 0; }
.burger { display: none; font-size: 28px; cursor: pointer; }
@media (max-width: 700px) {
  .burger { display: block; }
  .menu { display: none; flex-direction: column; padding: 12px 0; }
  #menu-toggle:checked ~ .menu { display: flex; }
}
```
