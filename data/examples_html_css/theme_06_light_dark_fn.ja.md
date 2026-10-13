# HTML/CSS の例: light-dark() 関数

1つの値でライトとダークの色を指定。

```html
<p class="note">Note</p>
```

```css
:root { color-scheme: light dark; }
.note { background: light-dark(#fef9c3, #3f3a12); color: light-dark(#713f12, #fde68a);
  padding: 12px 16px; border-radius: 10px; }
```
