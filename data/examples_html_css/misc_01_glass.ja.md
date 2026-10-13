# HTML/CSS の例: ガラス風エフェクト

背景をぼかす半透明パネル。

```html
<div class="glass">Glass panel</div>
```

```css
.glass { padding: 24px; border-radius: 20px; color: #fff;
  background: rgb(255 255 255 / .15); border: 1px solid rgb(255 255 255 / .3);
  backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); }
```
