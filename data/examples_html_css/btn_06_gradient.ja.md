# HTML/CSS の例: グラデーションボタン

グラデーションと影のピル型ボタン。

```html
<a class="btn-grad" href="#signup">Try for free</a>
```

```css
.btn-grad {
  display: inline-block; padding: 14px 28px; border-radius: 999px;
  background: linear-gradient(135deg, #8a5cff, #3fa2ff); color: #fff;
  text-decoration: none; font-weight: 700;
  box-shadow: 0 8px 24px rgb(91 107 255 / .35); transition: transform .2s, box-shadow .2s;
}
.btn-grad:hover { transform: translateY(-2px); box-shadow: 0 12px 28px rgb(91 107 255 / .45); }
```
