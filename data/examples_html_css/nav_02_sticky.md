# Пример HTML/CSS: липкая шапка с размытием

Шапка остаётся вверху при прокрутке, фон размыт.

```html
<header class="sticky-header">…</header>
```

```css
.sticky-header {
  position: sticky; top: 0; z-index: 50;
  display: flex; align-items: center; justify-content: space-between;
  padding: 12px 24px;
  background: rgb(255 255 255 / .8);
  backdrop-filter: saturate(180%) blur(10px);
  border-bottom: 1px solid rgb(0 0 0 / .06);
}
```
