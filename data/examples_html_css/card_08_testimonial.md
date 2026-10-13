# Пример HTML/CSS: карточка отзыва

Цитата, автор и аватар.

```html
<figure class="quote">
  <blockquote>"The best tool our team adopted this year."</blockquote>
  <figcaption><img src="a.jpg" alt=""><span><b>Kenji Sato</b><br>CTO, Acme</span></figcaption>
</figure>
```

```css
.quote { max-width: 420px; margin: 0; padding: 24px; border-radius: 16px; background: #f8f8fb; }
.quote blockquote { margin: 0 0 16px; font-size: 18px; line-height: 1.5; }
.quote figcaption { display: flex; align-items: center; gap: 12px; font-size: 14px; color: #555; }
.quote img { width: 40px; height: 40px; border-radius: 50%; object-fit: cover; }
```
