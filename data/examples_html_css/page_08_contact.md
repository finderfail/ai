# Пример HTML/CSS: страница контактов

Форма и информация в две колонки.

```html
<section class="contact"><div><h1>Contact us</h1><p>Answer within one business day.</p></div>
<form><input placeholder="Name" required><input type="email" placeholder="Email" required>
<textarea rows="5" placeholder="Message"></textarea><button>Send</button></form></section>
```

```css
.contact { display: grid; gap: 32px; max-width: 960px; margin: 48px auto; padding: 0 16px; }
@media (min-width: 768px) { .contact { grid-template-columns: 1fr 1.2fr; } }
.contact form { display: grid; gap: 12px; }
.contact input, .contact textarea { padding: 12px; border: 1px solid #d1d5db; border-radius: 10px; }
.contact button { padding: 12px; border: 0; border-radius: 10px; background: #4f46e5; color: #fff; }
```
