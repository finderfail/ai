# CSS：最近の機能

- **ネスト**（プリプロセッサ不要）：
```css
.card {
  padding: 16px;
  & h2 { margin: 0; }
  &:hover { box-shadow: 0 4px 16px rgb(0 0 0 / .1); }
}
```
- **:has()**：「親セレクター」：`.form:has(input:invalid) .submit { opacity: .5; }`。
- **カスケードレイヤー**：`@layer reset, base, components;` で、詳細度の争いなしに優先順位を決める。
- **aspect-ratio**：`.video { aspect-ratio: 16 / 9; }`。
- **論理プロパティ**：`margin-inline`、`padding-block`、`inset-inline-start`。右から左の文字にも対応。
- **object-fit**：`img { object-fit: cover; }`。
- **scroll-snap**：カルーセル用の `scroll-snap-type: x mandatory;`。
- **accent-color**：チェックボックスやラジオボタンの色を1行で。
- **color-mix()**：`color-mix(in srgb, #7b5cff 40%, white)`。

新しい機能を使う前に、ブラウザの対応状況（caniuse.com）を確認する。
