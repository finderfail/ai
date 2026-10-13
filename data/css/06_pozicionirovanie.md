# CSS: позиционирование и z-index

```css
.static   { position: static; }     /* по умолчанию, в потоке */
.relative { position: relative; top: 10px; }  /* смещение, место в потоке сохраняется */
.parent   { position: relative; }
.badge    { position: absolute; top: 0; right: 0; }  /* относительно ближайшего позиционированного предка */
.header   { position: fixed; top: 0; inset-inline: 0; } /* относительно окна, не прокручивается */
.toc      { position: sticky; top: 16px; } /* прилипает при прокрутке */
```

- `absolute` убирает элемент из потока и отсчитывается от ближайшего предка с `position` не `static`.
- `inset: 0` — все четыре стороны в 0.
- `sticky` не работает без `top` или при `overflow: hidden` у предка.
- `z-index` действует только на позиционированные элементы (и flex/grid-элементы). Он сравнивается **внутри контекста наложения**: `opacity < 1`, `transform`, `filter`, `position` с `z-index` создают новый контекст — поэтому `z-index: 9999` иногда «не работает».
