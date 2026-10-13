# HTML/CSS の例: 検証のスタイル

操作後にだけエラーを強調する。

```html
<label>Email<input type="email" required></label>
<p class="hint">Enter a valid email</p>
```

```css
input:user-invalid { border-color: #dc2626; background: #fef2f2; }
input:user-invalid + .hint, label:has(input:user-invalid) + .hint { display: block; }
.hint { display: none; margin: 4px 0 0; color: #dc2626; font-size: 13px; }
input:valid:not(:placeholder-shown) { border-color: #16a34a; }
```
