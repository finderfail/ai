# Пример HTML/CSS: уважение к reduced motion

Отключение анимаций для тех, кто это выбрал в системе.

```html
<div class="animated">…</div>
```

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: .01ms !important; animation-iteration-count: 1 !important;
    transition-duration: .01ms !important; scroll-behavior: auto !important;
  }
}
```
