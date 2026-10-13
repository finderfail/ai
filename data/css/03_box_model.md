# CSS: блочная модель (box model)

Каждый элемент — прямоугольник из слоёв: **content → padding → border → margin**.

```css
.card {
  width: 300px;
  padding: 16px;              /* внутренний отступ */
  border: 1px solid #ddd;
  margin: 24px auto;          /* внешний отступ; auto по бокам центрирует блок */
}

*, *::before, *::after {
  box-sizing: border-box;
}
```

- По умолчанию `box-sizing: content-box`: `width` — ширина только содержимого, и итоговая ширина = 300 + 2·16 + 2·1 = 334px.
- `box-sizing: border-box`: `width` включает padding и border — итог ровно 300px. Обычно его задают для всех элементов.
- **Схлопывание margin**: вертикальные отступы соседних блоков не складываются, берётся больший. Не происходит во flex/grid-контейнерах.
- Сокращения: `margin: 10px 20px` (верх/низ, лево/право), `margin: 1px 2px 3px 4px` (по часовой стрелке от верха).
- `display: block` занимает всю ширину, `inline` — по содержимому без width/height, `inline-block` — в строке, но с размерами.
