# HTML5：canvas と SVG

**canvas**：JavaScript によるラスター描画：
```html
<canvas id="c" width="300" height="150"></canvas>
<script>
  const ctx = document.getElementById('c').getContext('2d');
  ctx.fillStyle = '#7b5cff';
  ctx.fillRect(10, 10, 100, 50);
  ctx.beginPath();
  ctx.arc(200, 75, 40, 0, Math.PI * 2);
  ctx.fill();
  ctx.font = '16px sans-serif';
  ctx.fillText('こんにちは', 10, 120);
</script>
```

**SVG**：HTML に直接書けるベクター画像：
```html
<svg width="120" height="120" viewBox="0 0 120 120" role="img" aria-label="ロゴ">
  <circle cx="60" cy="60" r="50" fill="#7b5cff"/>
  <path d="M40 60 L55 75 L85 45" stroke="#fff" stroke-width="8" fill="none"/>
</svg>
```

- SVG は画質を落とさず拡大縮小でき、CSS でスタイルを付けられ、アイコンやロゴに向く。
- canvas は大量のオブジェクト（ゲーム、グラフ）に速いが、スクリーンリーダーからは読めない。
