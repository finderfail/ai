# CSS: как отцентрировать элемент

По горизонтали блок известной ширины:
```css
.box { width: 600px; margin-inline: auto; }
```

Текст и inline-элементы:
```css
.text { text-align: center; }
```

Flexbox — по обеим осям:
```css
.parent { display: flex; justify-content: center; align-items: center; min-height: 100vh; }
```

Grid — короче всего:
```css
.parent { display: grid; place-items: center; min-height: 100vh; }
```

Абсолютное позиционирование:
```css
.parent { position: relative; }
.child  { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); }
```

Модальное окно по центру экрана:
```css
.modal { position: fixed; inset: 0; margin: auto; width: min(90vw, 500px); height: fit-content; }
```

Для вертикального центрирования у родителя должна быть высота (`min-height`).
