# HTML5: глобальные и data-атрибуты

Глобальные атрибуты (у любого элемента):
- `id`, `class`, `style`, `title`, `lang`, `dir`;
- `hidden` — скрыть элемент;
- `tabindex` — порядок фокуса (`0` — в обычном порядке, `-1` — только программно);
- `contenteditable` — редактируемый блок;
- `draggable` — перетаскивание;
- `inert` — элемент и потомки неактивны и недоступны;
- `translate="no"` — не переводить;
- `spellcheck`, `autocapitalize`, `enterkeyhint`.

**data-атрибуты** — свои данные для JS и CSS:
```html
<button class="buy" data-product-id="42" data-price="1990">Купить</button>
<script>
  const btn = document.querySelector('.buy');
  btn.dataset.productId;   // "42"
  btn.dataset.price;       // "1990"
</script>
<style> [data-state="open"] { display: block; } </style>
```

Имена в `data-` пишутся через дефис, в `dataset` — в camelCase. Значения всегда строки.
