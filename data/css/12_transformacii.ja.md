# CSS：トランスフォーム

```css
.a { transform: translate(20px, 10px); }
.b { transform: scale(1.1); }
.c { transform: rotate(45deg); }
.d { transform: skew(10deg); }
.e { transform: translate(-50%, -50%) rotate(10deg) scale(0.9); }
.f { transform-origin: top left; }

.card { perspective: 800px; }
.card-inner { transform: rotateY(180deg); transform-style: preserve-3d; transition: transform 0.6s; }
.card-back { backface-visibility: hidden; }

.g { translate: 0 10px; rotate: 5deg; scale: 1.05; }
```

- トランスフォームは流れに影響せず、隣の要素は動かない。
- 関数の順序が重要：`translate` → `rotate` と `rotate` → `translate` は結果が違う。
- 個別プロパティ `translate`、`rotate`、`scale` はアニメーションで組み合わせやすい。
- `transform` を持つ要素は新しい重ね合わせコンテキストを作り、子孫の `position: fixed` の基準になる。
