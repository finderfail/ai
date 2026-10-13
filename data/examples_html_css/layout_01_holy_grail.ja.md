# HTML/CSS の例: ホーリーグレイルレイアウト

CSS Grid でヘッダー、メニュー、本文、サイドバー、フッター。

```html
<div class="page">
  <header>Header</header><nav>Nav</nav><main>Main</main><aside>Aside</aside><footer>Footer</footer>
</div>
```

```css
.page { display: grid; min-height: 100vh; gap: 12px;
  grid-template: "header header header" auto "nav main aside" 1fr "footer footer footer" auto / 200px 1fr 240px; }
header { grid-area: header; } nav { grid-area: nav; } main { grid-area: main; }
aside { grid-area: aside; } footer { grid-area: footer; }
@media (max-width: 800px) {
  .page { grid-template: "header" "nav" "main" "aside" "footer" / 1fr; }
}
```
