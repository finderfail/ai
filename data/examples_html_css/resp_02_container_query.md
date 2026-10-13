# Пример HTML/CSS: карточка на контейнерных запросах

Карточка меняет вид по ширине своего контейнера.

```html
<div class="slot"><article class="cq-card"><img src="a.jpg" alt=""><div>Text</div></article></div>
```

```css
.slot { container-type: inline-size; }
.cq-card { display: grid; gap: 12px; }
.cq-card img { width: 100%; border-radius: 10px; }
@container (min-width: 420px) {
  .cq-card { grid-template-columns: 160px 1fr; align-items: center; }
}
```
