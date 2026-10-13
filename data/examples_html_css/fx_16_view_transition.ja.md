# HTML/CSS の例: ページ遷移のアニメーション

JS なしのページ間トランジション（View Transitions）。

```html
<a href="/about">About</a>
```

```css
@view-transition { navigation: auto; }
::view-transition-old(root), ::view-transition-new(root) { animation-duration: .25s; }
```
