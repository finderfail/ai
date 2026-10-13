# Пример HTML/CSS: прижатый подвал

Подвал внизу экрана даже при малом количестве контента.

```html
<body><header>…</header><main>…</main><footer>…</footer></body>
```

```css
body { min-height: 100vh; margin: 0; display: grid; grid-template-rows: auto 1fr auto; }
```
