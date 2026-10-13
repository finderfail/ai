# Пример HTML/CSS: простая карточка

Карточка с заголовком, текстом и кнопкой.

```html
<article class="card">
  <h3>Starter plan</h3>
  <p>Everything you need to launch a small project.</p>
  <a href="#" class="card-link">Choose</a>
</article>
```

```css
.card { max-width: 320px; padding: 24px; border: 1px solid #e3e4e8;
  border-radius: 16px; background: #fff; box-shadow: 0 4px 16px rgb(0 0 0 / .06); }
.card h3 { margin: 0 0 8px; }
.card p { margin: 0 0 16px; color: #555; }
.card-link { font-weight: 600; color: #4f46e5; text-decoration: none; }
```
