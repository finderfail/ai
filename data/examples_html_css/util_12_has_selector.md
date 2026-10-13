# Пример HTML/CSS: стили родителя через :has()

Карточка подсвечивается, если внутри отмечен чекбокс.

```html
<label class="option"><input type="checkbox"> Extra storage</label>
```

```css
.option { display: flex; gap: 10px; padding: 14px; border: 1px solid #e5e7eb; border-radius: 12px; cursor: pointer; }
.option:has(input:checked) { border-color: #4f46e5; background: #eef2ff; }
```
