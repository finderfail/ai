# Пример HTML/CSS: всплывающее уведомление (toast)

Тост в углу экрана с анимацией появления.

```html
<div class="toast" role="status">Link copied</div>
```

```css
.toast { position: fixed; right: 16px; bottom: 16px; padding: 12px 16px; border-radius: 12px;
  background: #111; color: #fff; box-shadow: 0 8px 24px rgb(0 0 0 / .2);
  animation: toast-in .3s ease-out both, toast-out .3s ease-in 3s forwards; }
@keyframes toast-in { from { opacity: 0; transform: translateY(12px); } }
@keyframes toast-out { to { opacity: 0; transform: translateY(12px); } }
```
