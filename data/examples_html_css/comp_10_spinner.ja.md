# HTML/CSS の例: スピナー

CSS のリング型ローダー。

```html
<div class="spinner" role="status" aria-label="Loading"></div>
```

```css
.spinner { width: 40px; height: 40px; border-radius: 50%; border: 4px solid #e5e7eb;
  border-top-color: #4f46e5; animation: spin .8s linear infinite; }
@keyframes spin { to { transform: rotate(360deg); } }
@media (prefers-reduced-motion: reduce) { .spinner { animation-duration: 3s; } }
```
