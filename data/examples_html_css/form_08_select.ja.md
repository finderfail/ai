# HTML/CSS の例: スタイル付き select

独自の矢印を持つネイティブ select。

```html
<select class="select"><option>Japan</option><option>Belarus</option></select>
```

```css
.select {
  appearance: none; padding: 12px 40px 12px 14px; border: 1px solid #ccc; border-radius: 10px; font: inherit;
  background: #fff url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%23666' stroke-width='2' fill='none'/%3E%3C/svg%3E") no-repeat right 14px center;
}
```
