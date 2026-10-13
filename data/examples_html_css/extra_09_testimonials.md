# Пример HTML/CSS: отзывы клиентов

Карточки с цитатой и автором.

```html
<figure class="quote"><blockquote>Fast and reliable.</blockquote><figcaption>— Ken, CTO</figcaption></figure>
```

```css
.quote { margin: 0; padding: 24px; border-radius: 16px; background: #f9fafb; }
.quote blockquote { margin: 0 0 12px; font-size: 18px; line-height: 1.5; }
.quote blockquote::before { content: "“"; font-size: 40px; line-height: 0; vertical-align: -14px; color: #4f46e5; }
.quote figcaption { color: #6b7280; font-size: 14px; }
```
