# Пример HTML/CSS: список с галочками

Маркированный список с иконками-галочками.

```html
<ul class="checks"><li>Free updates</li><li>Email support</li><li>Cancel anytime</li></ul>
```

```css
.checks { list-style: none; padding: 0; }
.checks li { position: relative; padding-left: 28px; margin: 8px 0; }
.checks li::before { content: "✓"; position: absolute; left: 0; top: 0; width: 20px; height: 20px;
  display: grid; place-items: center; border-radius: 50%; background: #dcfce7; color: #16a34a; font-size: 12px; font-weight: 700; }
```
