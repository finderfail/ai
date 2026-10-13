# Пример HTML/CSS: все способы центрирования

Flex, grid, absolute и margin auto.

```html
<div class="box"><div class="item">Center</div></div>
```

```css
.box { display: grid; place-items: center; }
.box-flex { display: flex; justify-content: center; align-items: center; }
.box-abs { position: relative; } .box-abs .item { position: absolute; inset: 0; margin: auto; width: fit-content; height: fit-content; }
.block-center { width: min(100%, 720px); margin-inline: auto; }
.text-center { text-align: center; }
```
