# Пример HTML/CSS: растущий textarea

Поле, которое растёт по мере ввода (новые браузеры).

```html
<textarea class="auto" rows="1" placeholder="Write a message…"></textarea>
```

```css
.auto { width: 100%; field-sizing: content; min-height: 44px; max-height: 240px;
  padding: 10px 14px; border: 1px solid #ccc; border-radius: 14px; resize: none; font: inherit; }
```
