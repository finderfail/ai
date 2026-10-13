# HTML/CSS の例: スケルトンローダー

光沢が流れるコンテンツのプレースホルダー。

```html
<div class="sk sk-title"></div><div class="sk sk-line"></div><div class="sk sk-line short"></div>
```

```css
.sk { border-radius: 8px; margin-bottom: 10px;
  background: linear-gradient(90deg, #eee 25%, #f6f6f6 50%, #eee 75%) 0 0 / 200% 100%;
  animation: shimmer 1.4s infinite; }
.sk-title { height: 24px; width: 50%; } .sk-line { height: 14px; } .short { width: 70%; }
@keyframes shimmer { to { background-position: -200% 0; } }
```
