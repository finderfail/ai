# HTML/CSS の例: dialog のモーダル

背景を暗くするネイティブのモーダル。

```html
<dialog id="dlg"><form method="dialog"><p>Delete file?</p><button value="no">Cancel</button><button value="yes">Delete</button></form></dialog>
<button onclick="dlg.showModal()">Open</button>
```

```css
dialog { border: 0; border-radius: 16px; padding: 24px; max-width: 360px; box-shadow: 0 20px 50px rgb(0 0 0 / .25); }
dialog::backdrop { background: rgb(0 0 0 / .45); backdrop-filter: blur(2px); }
dialog form { display: flex; flex-wrap: wrap; gap: 8px; justify-content: flex-end; }
dialog p { flex-basis: 100%; margin: 0 0 12px; }
```
