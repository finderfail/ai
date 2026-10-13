# HTML/CSS の例: カード型ラジオボタン

ラジオボタンでプランをカード選択。

```html
<fieldset class="choices">
  <label><input type="radio" name="plan" checked><span>Monthly<br><b>$12</b></span></label>
  <label><input type="radio" name="plan"><span>Yearly<br><b>$120</b></span></label>
</fieldset>
```

```css
.choices { display: flex; gap: 12px; border: 0; padding: 0; }
.choices input { position: absolute; opacity: 0; }
.choices span { display: block; padding: 16px 20px; border: 2px solid #e5e7eb; border-radius: 14px; cursor: pointer; }
.choices input:checked + span { border-color: #4f46e5; background: #eef2ff; }
.choices input:focus-visible + span { outline: 3px solid #a5b4fc; }
```
