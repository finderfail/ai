# HTML/CSS の例: 設定ページ

ラベルとスイッチの行。

```html
<section class="settings">
  <label class="row"><span><b>Notifications</b><small>Email me about updates</small></span><input type="checkbox" role="switch"></label>
  <label class="row"><span><b>Language</b></span><select><option>English</option><option>日本語</option></select></label>
</section>
```

```css
.settings { max-width: 640px; border: 1px solid #e5e7eb; border-radius: 14px; }
.row { display: flex; justify-content: space-between; align-items: center; gap: 16px; padding: 16px 20px; }
.row + .row { border-top: 1px solid #e5e7eb; }
.row small { display: block; color: #6b7280; }
```
