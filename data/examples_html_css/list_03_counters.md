# Пример HTML/CSS: нумерация через counters

Свои номера шагов в кружках.

```html
<ol class="steps"><li>Sign up</li><li>Get a key</li><li>Connect</li></ol>
```

```css
.steps { list-style: none; counter-reset: step; padding: 0; }
.steps li { counter-increment: step; display: flex; align-items: center; gap: 12px; margin: 10px 0; }
.steps li::before { content: counter(step); display: grid; place-items: center; width: 28px; height: 28px;
  border-radius: 50%; background: #4f46e5; color: #fff; font-weight: 700; font-size: 14px; }
```
