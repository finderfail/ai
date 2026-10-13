# HTML/CSS の例: カスケードレイヤー @layer

reset・base・components・utilities の優先順。

```html
<button class="btn mt-0">OK</button>
```

```css
@layer reset, base, components, utilities;
@layer reset { * { margin: 0; } }
@layer base { body { font-family: system-ui, sans-serif; } }
@layer components { .btn { margin-top: 16px; padding: 8px 16px; } }
@layer utilities { .mt-0 { margin-top: 0; } }
```
