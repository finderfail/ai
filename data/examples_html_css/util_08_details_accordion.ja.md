# HTML/CSS の例: JS なしのアコーディオン

独自の矢印付き details/summary。

```html
<details class="acc"><summary>What is RAG?</summary><p>Retrieval-augmented generation…</p></details>
```

```css
.acc { border: 1px solid #e5e7eb; border-radius: 10px; padding: 12px 16px; }
.acc summary { cursor: pointer; font-weight: 600; list-style: none; display: flex; justify-content: space-between; }
.acc summary::-webkit-details-marker { display: none; }
.acc summary::after { content: "+"; } .acc[open] summary::after { content: "−"; }
```
