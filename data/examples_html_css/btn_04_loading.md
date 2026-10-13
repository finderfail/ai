# Пример HTML/CSS: кнопка с загрузкой

Кнопка со спиннером в состоянии загрузки (aria-busy).

```html
<button class="btn" aria-busy="true"><span class="spinner"></span>Saving…</button>
```

```css
.btn { display: inline-flex; align-items: center; gap: 8px; padding: 12px 20px;
  border: 0; border-radius: 10px; background: #4f46e5; color: #fff; }
.btn[aria-busy="true"] { opacity: .8; pointer-events: none; }
.spinner { width: 16px; height: 16px; border: 2px solid rgb(255 255 255 / .4);
  border-top-color: #fff; border-radius: 50%; animation: spin .8s linear infinite; }
@keyframes spin { to { transform: rotate(360deg); } }
```
