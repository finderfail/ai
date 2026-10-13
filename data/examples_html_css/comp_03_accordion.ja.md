# HTML/CSS の例: アコーディオン（FAQ）

details/summary による開閉式の質問。

```html
<details class="faq"><summary>How do I reset my password?</summary><p>Use the "Forgot password" link.</p></details>
<details class="faq"><summary>Can I cancel anytime?</summary><p>Yes, from account settings.</p></details>
```

```css
.faq { border-bottom: 1px solid #e5e7eb; padding: 12px 0; }
.faq summary { cursor: pointer; font-weight: 600; list-style: none; display: flex; justify-content: space-between; }
.faq summary::-webkit-details-marker { display: none; }
.faq summary::after { content: "+"; font-size: 20px; }
.faq[open] summary::after { content: "−"; }
.faq p { margin: 8px 0 0; color: #555; }
```
