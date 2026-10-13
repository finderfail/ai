# Пример HTML/CSS: плавающая кнопка действия

Круглая кнопка, закреплённая в правом нижнем углу.

```html
<button class="fab" aria-label="New message">+</button>
```

```css
.fab {
  position: fixed; right: 24px; bottom: calc(24px + env(safe-area-inset-bottom));
  width: 56px; height: 56px; border-radius: 50%; border: 0;
  background: #4f46e5; color: #fff; font-size: 28px; cursor: pointer;
  box-shadow: 0 6px 20px rgb(0 0 0 / .25);
}
```
