# HTML5: интерактивные элементы без JavaScript

```html
<details>
  <summary>Как сменить тариф?</summary>
  <p>Откройте настройки аккаунта…</p>
</details>

<dialog id="dlg">
  <form method="dialog">
    <p>Удалить файл?</p>
    <button value="cancel">Отмена</button>
    <button value="ok">Удалить</button>
  </form>
</dialog>
<button onclick="dlg.showModal()">Открыть диалог</button>

<button popovertarget="tip">Подсказка</button>
<div id="tip" popover>Текст всплывающей подсказки</div>

<template id="row">
  <li class="item"></li>
</template>

<progress value="70" max="100">70%</progress>
<meter value="0.6" min="0" max="1">60%</meter>
```

- `<details>` — раскрывающийся блок (FAQ, спойлеры).
- `<dialog>` с `showModal()` — модальное окно с затемнением и закрытием по Esc.
- `popover` — всплывающее окно без JS (новые браузеры).
- `<template>` — разметка, которую клонирует JavaScript.
