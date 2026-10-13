# HTML/CSS の例: ガラス風カード

backdrop-filter によるすりガラス効果。

```html
<div class="glass"><h3>Weather</h3><p>Tokyo · 21°C · Clear</p></div>
```

```css
body { min-height: 100vh; background: linear-gradient(135deg, #8a5cff, #3fa2ff); }
.glass {
  width: 280px; padding: 24px; border-radius: 20px; color: #fff;
  background: rgb(255 255 255 / .15);
  border: 1px solid rgb(255 255 255 / .3);
  backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
}
```
