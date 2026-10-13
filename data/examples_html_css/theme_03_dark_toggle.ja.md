# HTML/CSS の例: data-theme でテーマ切り替え

html の属性で手動テーマ選択。

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
