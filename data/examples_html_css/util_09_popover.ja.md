# HTML/CSS の例: JS なしの popover

popover 属性と開くボタン。

```html
<button popovertarget="menu">Menu</button>
<div id="menu" popover><a href="#">Profile</a><a href="#">Logout</a></div>
```

```css
#menu { padding: 8px; border: 1px solid #e5e7eb; border-radius: 12px; box-shadow: 0 10px 30px rgb(0 0 0 / .12); }
#menu a { display: block; padding: 8px 12px; border-radius: 8px; color: inherit; text-decoration: none; }
#menu a:hover { background: #f3f4f6; }
#menu::backdrop { background: transparent; }
```
