# Пример HTML/CSS: страница FAQ

Список вопросов на details.

```html
<section class="faq"><h2>FAQ</h2>
<details><summary>Can I cancel anytime?</summary><p>Yes.</p></details>
<details><summary>Is there a free plan?</summary><p>Yes, 10k tokens.</p></details></section>
```

```css
.faq { max-width: 720px; margin: auto; }
.faq details { border-bottom: 1px solid #e5e7eb; padding: 16px 0; }
.faq summary { cursor: pointer; font-weight: 600; }
.faq p { margin: 8px 0 0; color: #4b5563; }
```
