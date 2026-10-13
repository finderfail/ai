# HTML5：フォーム

```html
<form action="/signup" method="post">
  <label for="email">メールアドレス</label>
  <input id="email" name="email" type="email" required autocomplete="email">

  <label for="pass">パスワード</label>
  <input id="pass" name="password" type="password" minlength="8" required autocomplete="new-password">

  <fieldset>
    <legend>プラン</legend>
    <label><input type="radio" name="plan" value="free" checked> Free</label>
    <label><input type="radio" name="plan" value="pro"> Pro</label>
  </fieldset>

  <label><input type="checkbox" name="agree" required> 規約に同意する</label>

  <label for="country">国</label>
  <select id="country" name="country">
    <option value="jp" selected>日本</option>
    <option value="by">ベラルーシ</option>
  </select>

  <textarea name="comment" rows="4"></textarea>
  <button type="submit">登録する</button>
</form>
```

- 各フィールドに `<label>` を付ける（`for`/`id` か、囲む形で）。
- 値をサーバーに送るには `name` が必要。
- フォーム内の `<button>` は既定で `type="submit"`。
