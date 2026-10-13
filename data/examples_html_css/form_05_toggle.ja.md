# HTML/CSS の例: トグルスイッチ

チェックボックスをスイッチ風にする。

```html
<label class="switch"><input type="checkbox" role="switch"> Notifications</label>
```

```css
.switch { display: inline-flex; align-items: center; gap: 10px; cursor: pointer; }
.switch input { appearance: none; width: 44px; height: 24px; border-radius: 999px; background: #d1d5db;
  position: relative; transition: background .2s; cursor: pointer; }
.switch input::after { content: ""; position: absolute; top: 3px; left: 3px; width: 18px; height: 18px;
  border-radius: 50%; background: #fff; transition: transform .2s; }
.switch input:checked { background: #4f46e5; }
.switch input:checked::after { transform: translateX(20px); }
```
