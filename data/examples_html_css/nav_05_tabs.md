# Пример HTML/CSS: вкладки без JS

Переключение вкладок на радиокнопках.

```html
<div class="tabs">
  <input type="radio" name="t" id="t1" checked><label for="t1">Overview</label>
  <input type="radio" name="t" id="t2"><label for="t2">Specs</label>
  <div class="panel" id="p1">Overview content</div>
  <div class="panel" id="p2">Specs content</div>
</div>
```

```css
.tabs input { display: none; }
.tabs label { display: inline-block; padding: 10px 16px; cursor: pointer; border-bottom: 2px solid transparent; }
.tabs input:checked + label { border-color: #4f46e5; color: #4f46e5; font-weight: 600; }
.panel { display: none; padding: 16px 0; }
#t1:checked ~ #p1, #t2:checked ~ #p2 { display: block; }
```
