# Пример HTML/CSS: блок подписки на рассылку

Цветная секция с формой в строку.

```html
<section class="news"><h2>Stay in the loop</h2><form><input type="email" placeholder="Email" required><button>Subscribe</button></form></section>
```

```css
.news { padding: 40px 24px; border-radius: 20px; background: #4f46e5; color: #fff; text-align: center; }
.news form { display: flex; flex-wrap: wrap; gap: 8px; justify-content: center; margin-top: 16px; }
.news input { flex: 1 1 220px; max-width: 320px; padding: 12px 14px; border: 0; border-radius: 10px; }
.news button { padding: 12px 20px; border: 0; border-radius: 10px; background: #111; color: #fff; }
```
