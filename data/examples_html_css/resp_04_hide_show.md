# Пример HTML/CSS: показать/скрыть по ширине

Разные элементы для мобильных и десктопа.

```html
<span class="mobile-only">Menu</span><nav class="desktop-only">…</nav>
```

```css
.mobile-only { display: none; }
@media (max-width: 768px) {
  .mobile-only { display: inline; }
  .desktop-only { display: none; }
}
```
