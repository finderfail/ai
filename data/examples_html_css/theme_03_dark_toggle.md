# Пример HTML/CSS: переключатель темы через data-theme

Ручной выбор темы атрибутом на html.

```html
<html data-theme="dark">
<button onclick="document.documentElement.dataset.theme =
  document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark'">Theme</button>
```

```css
:root { --bg: #fff; --text: #111; }
:root[data-theme="dark"] { --bg: #111; --text: #eee; color-scheme: dark; }
body { background: var(--bg); color: var(--text); transition: background .2s, color .2s; }
```
