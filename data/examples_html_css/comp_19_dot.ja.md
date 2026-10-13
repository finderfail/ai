# HTML/CSS の例: 通知ドット

ベルアイコンの赤い点。

```html
<button class="bell" aria-label="Notifications, 3 new">🔔<span class="dot"></span></button>
```

```css
.bell { position: relative; border: 0; background: none; font-size: 24px; cursor: pointer; }
.dot { position: absolute; top: 2px; right: 2px; width: 10px; height: 10px; border-radius: 50%;
  background: #ef4444; border: 2px solid #fff; }
```
