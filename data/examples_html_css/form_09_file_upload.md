# Пример HTML/CSS: загрузка файла

Красивая зона загрузки поверх input type=file.

```html
<label class="drop">
  <input type="file" accept="image/*" hidden>
  <span>Drop an image or <u>browse</u></span>
</label>
```

```css
.drop { display: grid; place-items: center; height: 160px; padding: 16px; border: 2px dashed #c7c9d1;
  border-radius: 16px; color: #555; cursor: pointer; text-align: center; transition: border-color .2s, background .2s; }
.drop:hover { border-color: #4f46e5; background: #f5f7ff; }
```
