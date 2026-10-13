# HTML/CSS の例: キーとコードの表示

キーとインラインコードのスタイル。

```html
<p>Press <kbd>Ctrl</kbd> + <kbd>K</kbd> to search. Run <code>npm start</code>.</p>
```

```css
kbd { padding: 2px 6px; border: 1px solid #ccc; border-bottom-width: 2px; border-radius: 6px;
  background: #f9fafb; font: 13px ui-monospace, monospace; }
code { padding: 2px 6px; border-radius: 6px; background: #f3f4f6; font: 0.9em ui-monospace, monospace; }
```
