# HTML/CSS の例: モダンなベースリセット

新規プロジェクト用の最小リセット。

```html
<!doctype html>
```

```css
*, *::before, *::after { box-sizing: border-box; }
body { margin: 0; line-height: 1.5; -webkit-font-smoothing: antialiased; }
img, picture, video, canvas, svg { display: block; max-width: 100%; }
input, button, textarea, select { font: inherit; }
p, h1, h2, h3 { overflow-wrap: break-word; }
h1, h2, h3 { line-height: 1.2; text-wrap: balance; }
```
