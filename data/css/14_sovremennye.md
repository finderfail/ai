# CSS: современные возможности

- **Вложенность (nesting)** без препроцессоров:
```css
.card {
  padding: 16px;
  & h2 { margin: 0; }
  &:hover { box-shadow: 0 4px 16px rgb(0 0 0 / .1); }
}
```
- **:has()** — «родительский селектор»: `.form:has(input:invalid) .submit { opacity: .5; }`.
- **Каскадные слои**: `@layer reset, base, components;` — порядок важности без борьбы специфичностей.
- **aspect-ratio**: `.video { aspect-ratio: 16 / 9; }`.
- **Логические свойства**: `margin-inline`, `padding-block`, `inset-inline-start` — работают и для письма справа налево.
- **object-fit**: `img { object-fit: cover; }`.
- **scroll-snap**: `scroll-snap-type: x mandatory;` для каруселей.
- **accent-color**: цвет чекбоксов и радиокнопок одной строкой.
- **color-mix()**: `color-mix(in srgb, #7b5cff 40%, white)`.

Перед использованием новых возможностей проверяйте поддержку браузерами (caniuse.com).
