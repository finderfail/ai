# Пример HTML/CSS: тёмная тема по настройке системы

prefers-color-scheme переопределяет переменные.

```html
<body>…</body>
```

```css
:root { color-scheme: light dark; --bg: #fff; --text: #111; --muted: #6b7280; --card: #f9fafb; }
@media (prefers-color-scheme: dark) {
  :root { --bg: #0f1115; --text: #e5e7eb; --muted: #9ca3af; --card: #1a1d24; }
}
body { background: var(--bg); color: var(--text); }
.card { background: var(--card); }
```
