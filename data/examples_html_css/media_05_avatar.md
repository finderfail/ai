# Пример HTML/CSS: круглый аватар с инициалами

Аватар-картинка и запасной вариант с буквами.

```html
<img class="avatar" src="me.jpg" alt="Ann Lee">
<span class="avatar initials" aria-label="Kenji Sato">KS</span>
```

```css
.avatar { width: 48px; height: 48px; border-radius: 50%; object-fit: cover; display: inline-grid;
  place-items: center; vertical-align: middle; }
.initials { background: #e0e7ff; color: #3730a3; font-weight: 700; }
```
