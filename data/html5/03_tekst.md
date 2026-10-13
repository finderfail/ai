# HTML5: текстовые элементы

```html
<h1>…</h1> … <h6>…</h6>          <!-- заголовки по уровням, без пропусков -->
<p>Абзац</p>
<strong>важно</strong> <em>акцент</em>
<b>жирный без смысла</b> <i>термин, иностранное слово</i>
<mark>выделение</mark> <small>мелкий текст</small>
<del>удалено</del> <ins>добавлено</ins> <s>неактуально</s>
<sub>2</sub> <sup>2</sup>
<abbr title="HyperText Markup Language">HTML</abbr>
<time datetime="2026-10-12">12 октября</time>
<code>npm install</code> <kbd>Ctrl</kbd>+<kbd>C</kbd>
<pre>  форматирование
  сохраняется</pre>
<blockquote cite="https://example.com">Цитата</blockquote>
<q>короткая цитата</q>
<br> <hr>
<address>Контакты автора</address>
```

- Используйте один `<h1>` на страницу и иерархию заголовков без пропусков.
- `<strong>`/`<em>` несут смысл, `<b>`/`<i>` — визуальное выделение.
- `<br>` — только для переноса внутри смыслового блока (адрес, стихи), не для отступов.
