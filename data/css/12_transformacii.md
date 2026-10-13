# CSS: трансформации

```css
.a { transform: translate(20px, 10px); }
.b { transform: scale(1.1); }
.c { transform: rotate(45deg); }
.d { transform: skew(10deg); }
.e { transform: translate(-50%, -50%) rotate(10deg) scale(0.9); }
.f { transform-origin: top left; }

.card { perspective: 800px; }
.card-inner { transform: rotateY(180deg); transform-style: preserve-3d; transition: transform 0.6s; }
.card-back { backface-visibility: hidden; }

.g { translate: 0 10px; rotate: 5deg; scale: 1.05; }
```

- Трансформации не влияют на поток: соседние элементы не сдвигаются.
- Порядок функций важен: `translate` затем `rotate` ≠ `rotate` затем `translate`.
- Отдельные свойства `translate`, `rotate`, `scale` удобнее комбинировать в анимациях.
- Элемент с `transform` создаёт новый контекст наложения и становится точкой отсчёта для `position: fixed` потомков.
