# Пример HTML/CSS: нижняя навигация для мобильных

Панель вкладок внизу экрана с safe-area.

```html
<nav class="bottom-nav">
  <a href="#" class="active">Home</a><a href="#">Search</a><a href="#">Profile</a>
</nav>
```

```css
.bottom-nav { position: fixed; left: 0; right: 0; bottom: 0; display: grid; grid-template-columns: repeat(3, 1fr);
  padding-bottom: env(safe-area-inset-bottom); background: #fff; border-top: 1px solid #eee; }
.bottom-nav a { padding: 12px 0; text-align: center; color: #777; text-decoration: none; font-size: 13px; }
.bottom-nav a.active { color: #4f46e5; font-weight: 600; }
```
