# HTML/CSS の例: 料金比較表

おすすめ列を強調した料金の比較。

```html
<table class="compare"><tr><th></th><th>Free</th><th class="hl">Pro</th></tr>
<tr><td>Tokens</td><td>10k</td><td class="hl">1M</td></tr>
<tr><td>API</td><td>—</td><td class="hl">✓</td></tr></table>
```

```css
.compare { border-collapse: collapse; text-align: center; }
.compare th, .compare td { padding: 12px 20px; border-bottom: 1px solid #eee; }
.compare td:first-child { text-align: left; color: #555; }
.compare .hl { background: #eef2ff; font-weight: 600; }
```
