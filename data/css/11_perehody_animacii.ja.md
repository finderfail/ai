# CSS：トランジションとアニメーション

**トランジション**：状態が変わるときにプロパティをなめらかに変える：
```css
.button {
  background: #7b5cff;
  transition: background-color 0.2s ease, transform 0.2s ease;
}
.button:hover { background: #6440f5; transform: translateY(-2px); }
```

**アニメーション（@keyframes）**：自動で再生される：
```css
@keyframes spin { to { transform: rotate(360deg); } }
.loader { animation: spin 1s linear infinite; }

@keyframes fade-in {
  from { opacity: 0; transform: translateY(8px); }
  to   { opacity: 1; transform: none; }
}
.toast { animation: fade-in 0.3s ease-out both; }
```

- `transform` と `opacity` をアニメーションさせる。ブラウザがレイアウトの再計算なしに GPU で処理できる。`width`、`top`、`margin` はコストが高い。
- `prefers-reduced-motion` を尊重する。
- タイミング関数：`ease`、`linear`、`ease-in-out`、`cubic-bezier()`、`steps()`。
