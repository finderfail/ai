# HTML/CSS の例: 縦型タイムライン

時間軸上のイベント。

```html
<ol class="timeline">
  <li><time>2022</time><p>Project started</p></li>
  <li><time>2025</time><p>New website launched</p></li>
</ol>
```

```css
.timeline { list-style: none; padding: 0 0 0 24px; border-left: 2px solid #e5e7eb; }
.timeline li { position: relative; margin-bottom: 24px; }
.timeline li::before { content: ""; position: absolute; left: -31px; top: 4px; width: 12px; height: 12px;
  border-radius: 50%; background: #4f46e5; border: 2px solid #fff; }
.timeline time { font-weight: 700; } .timeline p { margin: 4px 0 0; color: #555; }
```
