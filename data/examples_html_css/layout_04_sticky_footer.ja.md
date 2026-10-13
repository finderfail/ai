# HTML/CSS の例: 下部固定フッター

内容が少なくても画面下にフッターを置く。

```html
<body><header>…</header><main>…</main><footer>…</footer></body>
```

```css
body { min-height: 100vh; margin: 0; display: grid; grid-template-rows: auto 1fr auto; }
```
