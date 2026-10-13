# Пример HTML/CSS: контактная форма

Имя, почта, тема и сообщение в сетке.

```html
<form class="contact">
  <input name="name" placeholder="Name" required><input name="email" type="email" placeholder="Email" required>
  <input name="subject" placeholder="Subject" class="full">
  <textarea name="message" rows="5" placeholder="Message" class="full" required></textarea>
  <button class="full">Send</button>
</form>
```

```css
.contact { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; max-width: 600px; }
.contact .full { grid-column: 1 / -1; }
.contact input, .contact textarea { padding: 12px; border: 1px solid #ccc; border-radius: 10px; font: inherit; }
.contact button { padding: 12px; border: 0; border-radius: 10px; background: #4f46e5; color: #fff; }
@media (max-width: 560px) { .contact { grid-template-columns: 1fr; } }
```
