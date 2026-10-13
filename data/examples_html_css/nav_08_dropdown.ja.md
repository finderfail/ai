# HTML/CSS の例: ドロップダウンメニュー

hover とキーボードフォーカスで開くサブメニュー。

```html
<ul class="menubar">
  <li class="has-sub"><a href="#">Products</a>
    <ul class="sub"><li><a href="#">Analytics</a></li><li><a href="#">Storage</a></li></ul>
  </li>
</ul>
```

```css
.menubar, .sub { list-style: none; margin: 0; padding: 0; }
.has-sub { position: relative; }
.sub { position: absolute; top: 100%; left: 0; min-width: 180px; padding: 8px; background: #fff;
  border-radius: 10px; box-shadow: 0 8px 24px rgb(0 0 0 / .12); display: none; }
.has-sub:hover .sub, .has-sub:focus-within .sub { display: block; }
.sub a { display: block; padding: 8px 10px; border-radius: 6px; }
```
