# Пример HTML/CSS: плавная прокрутка к якорям

Плавный скролл и отступ под липкую шапку.

```html
<a href="#pricing">Pricing</a> … <section id="pricing">…</section>
```

```css
html { scroll-behavior: smooth; scroll-padding-top: 80px; }
@media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } }
```
