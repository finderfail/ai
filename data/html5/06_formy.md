# HTML5: формы

```html
<form action="/signup" method="post">
  <label for="email">Почта</label>
  <input id="email" name="email" type="email" required autocomplete="email">

  <label for="pass">Пароль</label>
  <input id="pass" name="password" type="password" minlength="8" required autocomplete="new-password">

  <fieldset>
    <legend>Тариф</legend>
    <label><input type="radio" name="plan" value="free" checked> Free</label>
    <label><input type="radio" name="plan" value="pro"> Pro</label>
  </fieldset>

  <label><input type="checkbox" name="agree" required> Согласен с условиями</label>

  <label for="country">Страна</label>
  <select id="country" name="country">
    <option value="jp">Япония</option>
    <option value="by" selected>Беларусь</option>
  </select>

  <button type="submit">Зарегистрироваться</button>
</form>
```

- Каждому полю — `<label>`.
- `name` нужен, чтобы значение отправилось на сервер.
- `<button>` внутри формы по умолчанию `type="submit"`.
