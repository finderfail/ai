# HTML5: типы input и валидация

Типы: `text`, `email`, `password`, `tel`, `url`, `number`, `range`, `date`, `time`, `datetime-local`, `month`, `week`, `color`, `search`, `file`, `hidden`, `checkbox`, `radio`.

```html
<input type="number" min="1" max="10" step="1">
<input type="range" min="0" max="100" value="50">
<input type="date" min="2026-01-01">
<input type="tel" pattern="[0-9+ -]{7,20}" inputmode="tel">
<input type="file" accept="image/*" multiple>
<input type="text" required maxlength="50" placeholder="Имя">
<input type="text" inputmode="numeric" autocomplete="one-time-code">
<output name="result">0</output>
```

- Встроенная валидация: `required`, `min`/`max`, `minlength`/`maxlength`, `pattern`, `type="email"`.
- CSS: `:invalid`, `:user-invalid` (после взаимодействия), `:valid`.
- **Валидацию на клиенте всегда дублируйте на сервере** — её легко обойти.
