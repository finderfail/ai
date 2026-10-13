# HTML5: списки и таблицы

```html
<ul><li>Маркированный</li></ul>
<ol start="3" reversed><li>Нумерованный</li></ol>
<dl><dt>Термин</dt><dd>Определение</dd></dl>

<table>
  <caption>Продажи по кварталам</caption>
  <thead>
    <tr><th scope="col">Квартал</th><th scope="col">Сумма</th></tr>
  </thead>
  <tbody>
    <tr><th scope="row">Q1</th><td>120 000</td></tr>
    <tr><th scope="row">Q2</th><td>150 000</td></tr>
  </tbody>
  <tfoot>
    <tr><th scope="row">Итого</th><td>270 000</td></tr>
  </tfoot>
</table>
```

- Таблицы — только для табличных данных, не для раскладки страницы.
- `<th scope>` и `<caption>` помогают скринридерам.
- Объединение ячеек: `colspan="2"`, `rowspan="3"`.
- Широкие таблицы на мобильных оборачивают в контейнер с `overflow-x: auto`.
