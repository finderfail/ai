# CSS：色、背景、枠線、影

**色：**`red`、`#7b5cff`、`#7b5cff80`（透明度付き）、`rgb(123 92 255 / 0.5)`、`hsl(255 100% 68%)`、`oklch(65% 0.2 285)`、`transparent`、`currentColor`。

```css
.card {
  background-color: #fff;
  background-image: url("bg.png");
  background-size: cover;            /* contain は全体を収める */
  background-position: center;
  background-repeat: no-repeat;
  border: 1px solid #e3e4e8;
  border-radius: 16px;               /* 角丸。50% で円 */
  box-shadow: 0 4px 24px rgb(0 0 0 / 0.08);
  opacity: 0.9;
}
.hero {
  background: linear-gradient(135deg, #8a5cff, #5b6bff);
}
.badge {
  background: radial-gradient(circle, #fff 0%, transparent 70%);
}
h1 { text-shadow: 0 2px 4px rgb(0 0 0 / 0.3); }
.outline { outline: 2px solid #7b5cff; outline-offset: 2px; }
```

- 角丸、影、グラデーション、RGBA/HSLA、複数背景は CSS3 で追加された。
- `opacity` は内容ごと要素全体を透明にする。背景だけ透明にするにはアルファ付きの色を使う。
