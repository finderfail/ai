# Пример HTML/CSS: оформление статьи

Читабельный текст статьи: ширина, интерлиньяж, отступы.

```html
<article class="prose"><h1>Title</h1><p>Text…</p><h2>Section</h2><p>Text…</p></article>
```

```css
.prose { max-width: 68ch; margin-inline: auto; font-size: 18px; line-height: 1.7; color: #222; }
.prose h1 { font-size: 2.2em; line-height: 1.15; margin: 0 0 .6em; }
.prose h2 { margin: 1.8em 0 .5em; line-height: 1.25; }
.prose p { margin: 0 0 1.1em; }
.prose a { color: #4f46e5; text-underline-offset: 3px; }
.prose img { max-width: 100%; border-radius: 12px; }
```
