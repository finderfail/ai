# CSS1: свойства шрифта и текста

**Шрифт:**
```css
P {
  font-family: "Times New Roman", serif;   /* serif, sans-serif, cursive, fantasy, monospace */
  font-style: italic;                      /* normal | italic | oblique */
  font-variant: small-caps;                /* normal | small-caps */
  font-weight: bold;                       /* normal | bold | bolder | lighter | 100–900 */
  font-size: 12pt;                         /* xx-small … xx-large, длина, % */
}
H1 { font: bold 24pt/1.2 Helvetica, sans-serif }   /* сокращённая запись */
```

**Текст:**
```css
P {
  word-spacing: 0.4em;
  letter-spacing: 0.1em;
  text-decoration: underline;   /* none | underline | overline | line-through | blink */
  vertical-align: super;        /* baseline | sub | super | top | middle | bottom | % */
  text-transform: uppercase;    /* capitalize | uppercase | lowercase | none */
  text-align: justify;          /* left | right | center | justify */
  text-indent: 3em;
  line-height: 1.5;
}
```
