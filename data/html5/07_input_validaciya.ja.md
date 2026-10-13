# HTML5：input の種類と検証

種類：`text`、`email`、`password`、`tel`、`url`、`number`、`range`、`date`、`time`、`datetime-local`、`month`、`week`、`color`、`search`、`file`、`hidden`、`checkbox`、`radio`。

```html
<input type="number" min="1" max="10" step="1">
<input type="range" min="0" max="100" value="50">
<input type="date" min="2026-01-01">
<input type="tel" pattern="[0-9+ -]{7,20}" inputmode="tel">
<input type="file" accept="image/*" multiple>
<input type="text" required maxlength="50" placeholder="名前">
<input list="cities"><datalist id="cities"><option value="ミンスク"><option value="東京"></datalist>
<input type="text" inputmode="numeric" autocomplete="one-time-code">
<output name="result">0</output>
```

- 組み込みの検証：`required`、`min`/`max`、`minlength`/`maxlength`、`pattern`、`type="email"`。
- CSS：`:invalid`、`:user-invalid`（操作後）、`:valid`。
- フォームの `novalidate` でブラウザの検証を無効にできる。
- **クライアント側の検証は必ずサーバー側でも行う**。簡単に回避できるため。
