# Пример HTML/CSS: чипы-фильтры

Выбираемые чипы на чекбоксах.

```html
<div class="chips">
  <label><input type="checkbox" checked><span>Design</span></label>
  <label><input type="checkbox"><span>Backend</span></label>
</div>
```

```css
.chips { display: flex; flex-wrap: wrap; gap: 8px; }
.chips input { position: absolute; opacity: 0; }
.chips span { display: inline-block; padding: 6px 14px; border: 1px solid #d1d5db; border-radius: 999px; cursor: pointer; }
.chips input:checked + span { background: #111; color: #fff; border-color: #111; }
```
