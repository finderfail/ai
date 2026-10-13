# HTML/CSS の例: サイトのフッター

リンクの列と著作権表示。

```html
<footer class="footer">
  <div><h4>Product</h4><a href="#">Features</a><a href="#">Pricing</a></div>
  <div><h4>Company</h4><a href="#">About</a><a href="#">Careers</a></div>
  <p class="copy">© 2026 Brand</p>
</footer>
```

```css
.footer { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 24px;
  padding: 40px 24px; background: #0f172a; color: #cbd5e1; }
.footer h4 { margin: 0 0 10px; color: #fff; }
.footer a { display: block; padding: 4px 0; color: inherit; text-decoration: none; }
.copy { grid-column: 1 / -1; margin: 16px 0 0; font-size: 14px; color: #64748b; }
```
