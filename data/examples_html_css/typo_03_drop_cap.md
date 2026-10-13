# Пример HTML/CSS: буквица

Крупная первая буква абзаца.

```html
<p class="drop">Once upon a time…</p>
```

```css
.drop::first-letter { float: left; font-size: 3.4em; line-height: .9; font-weight: 700;
  margin: .05em .1em 0 0; color: #4f46e5; }
.drop { initial-letter: 3; }
```
