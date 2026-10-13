# HTML/CSS の例: 入れ子の番号 1.1, 1.2

多階層のセクション番号。

```html
<ol class="toc"><li>Intro<ol><li>Goals</li><li>Scope</li></ol></li></ol>
```

```css
.toc, .toc ol { list-style: none; counter-reset: item; padding-left: 16px; }
.toc li { counter-increment: item; }
.toc li::before { content: counters(item, ".") ". "; color: #6b7280; }
```
