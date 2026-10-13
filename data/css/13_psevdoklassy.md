# CSS: псевдоклассы и псевдоэлементы

**Псевдоклассы** — состояние элемента:
```css
a:hover, a:focus-visible { text-decoration: underline; }
button:active { transform: scale(0.98); }
input:focus { outline: 2px solid #7b5cff; }
input:invalid { border-color: red; }
input:checked + label { font-weight: 600; }
input:disabled { opacity: 0.5; }
li:nth-child(odd) { background: #f5f5f7; }
p:empty { display: none; }
```

**Псевдоэлементы** — «виртуальные» части элемента (два двоеточия):
```css
.required::after { content: " *"; color: red; }
blockquote::before { content: "«"; }
p::first-letter { font-size: 2em; }
::selection { background: #efeaff; }
input::placeholder { color: #a3a5ad; }
li::marker { color: #7b5cff; }
```

- `::before` и `::after` требуют свойства `content`.
- `:focus-visible` показывает фокус только при навигации с клавиатуры.
