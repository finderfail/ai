# Пример HTML/CSS: вертикальная лента событий

Линия с точками и датами.

```html
<ol class="timeline"><li><time>2022</time> Project started</li><li><time>2025</time> New site</li></ol>
```

```css
.timeline { list-style: none; padding-left: 24px; border-left: 2px solid #e5e7eb; }
.timeline li { position: relative; margin: 0 0 20px; }
.timeline li::before { content: ""; position: absolute; left: -31px; top: 4px; width: 12px; height: 12px;
  border-radius: 50%; background: #4f46e5; border: 2px solid #fff; }
.timeline time { display: block; font-weight: 700; }
```
