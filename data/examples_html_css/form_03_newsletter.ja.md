# HTML/CSS の例: 1行のニュースレター登録

入力欄とボタンを1行に。スマホでは縦並び。

```html
<form class="subscribe">
  <input type="email" placeholder="you@example.com" aria-label="Email" required>
  <button>Subscribe</button>
</form>
```

```css
.subscribe { display: flex; gap: 8px; max-width: 460px; }
.subscribe input { flex: 1; min-width: 0; padding: 12px 14px; border: 1px solid #ccc; border-radius: 10px; }
.subscribe button { padding: 12px 18px; border: 0; border-radius: 10px; background: #111; color: #fff; }
@media (max-width: 480px) { .subscribe { flex-direction: column; } }
```
