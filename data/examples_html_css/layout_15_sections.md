# Пример HTML/CSS: секции с чередующимся фоном

Секции лендинга с полноширинным фоном и узким контентом.

```html
<section class="band"><div class="inner">…</div></section>
<section class="band alt"><div class="inner">…</div></section>
```

```css
.band { padding: 80px 16px; }
.band.alt { background: #f8fafc; }
.inner { max-width: 960px; margin-inline: auto; }
```
