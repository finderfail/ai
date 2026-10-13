# CSS：タイポグラフィとフォント

```css
body {
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  font-size: 1rem;
  line-height: 1.6;
  color: #1c1c1f;
}
h1 { font-size: clamp(2rem, 5vw, 3.5rem); font-weight: 700; letter-spacing: -0.02em; }
p  { max-width: 65ch; text-align: left; }
.caps { text-transform: uppercase; }
.ellipsis { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.clamp-3 { display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }

@font-face {
  font-family: "Inter";
  src: url("/fonts/Inter.woff2") format("woff2");
  font-weight: 100 900;
  font-display: swap;
}
```

- 単位なしの `line-height`（1.5〜1.7）はフォントサイズに合わせて伸縮する。
- `font-display: swap` は独自フォントの読み込み中、システムフォントで文字を表示する。
- Web 用のフォント形式は WOFF2。
- 日本語には `font-family: "Hiragino Sans", "Noto Sans JP", sans-serif;` などを指定する。
