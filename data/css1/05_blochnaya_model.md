# CSS1: блочная модель и float

```css
P {
  margin: 1em 2em;                       /* margin-top/right/bottom/left */
  padding: 0.5em;
  border-width: thin;                    /* thin | medium | thick | длина */
  border-style: solid;                   /* none dotted dashed solid double groove ridge inset outset */
  border-color: gray;
  width: 50%;
  height: auto;
}
IMG.left  { float: left; margin-right: 1em }
DIV.after { clear: both }                /* left | right | both | none */
H2 { border-bottom: thin solid black }
```

- `width` и `height` задают размер **содержимого**; padding и border добавляются сверху (поведение content-box).
- Вертикальные margin соседних блоков схлопываются.
- `float` — единственный способ раскладки по колонкам в CSS1; позиционирования (`position`) ещё не было.
- В CSS1 описаны стили рамок `dotted` … `outset`, но браузеры того времени поддерживали их неполностью.
