# HTML/CSS の例: サイドバーメニュー

アイコンと現在の項目を持つ縦ナビゲーション。

```html
<nav class="side">
  <a href="#" class="active">Dashboard</a><a href="#">Projects</a><a href="#">Team</a><a href="#">Settings</a>
</nav>
```

```css
.side { display: flex; flex-direction: column; gap: 4px; width: 220px; padding: 12px; background: #f7f7f9; min-height: 100vh; }
.side a { padding: 10px 12px; border-radius: 10px; color: #444; text-decoration: none; }
.side a:hover { background: #ececf1; }
.side a.active { background: #fff; color: #111; font-weight: 600; box-shadow: 0 1px 2px rgb(0 0 0 / .06); }
```
