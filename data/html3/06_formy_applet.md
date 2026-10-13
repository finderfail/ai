# HTML 3.2: формы и апплеты

```html
<FORM ACTION="/cgi-bin/order.pl" METHOD=POST>
Имя: <INPUT TYPE=TEXT NAME="name" SIZE=30 MAXLENGTH=50><BR>
Пароль: <INPUT TYPE=PASSWORD NAME="pass"><BR>
<INPUT TYPE=CHECKBOX NAME="news" VALUE="yes" CHECKED> Подписка<BR>
<INPUT TYPE=RADIO NAME="pay" VALUE="card"> Карта
<INPUT TYPE=RADIO NAME="pay" VALUE="cash" CHECKED> Наличные<BR>
<SELECT NAME="color" SIZE=1>
  <OPTION VALUE="r">Красный
  <OPTION VALUE="g" SELECTED>Зелёный
</SELECT><BR>
<TEXTAREA NAME="comment" ROWS=4 COLS=40></TEXTAREA><BR>
<INPUT TYPE=FILE NAME="photo"> <INPUT TYPE=HIDDEN NAME="id" VALUE="42">
<INPUT TYPE=SUBMIT VALUE="Отправить"> <INPUT TYPE=RESET VALUE="Очистить">
</FORM>

<APPLET CODE="Clock.class" WIDTH=150 HEIGHT=50>
<PARAM NAME="color" VALUE="blue">Ваш браузер не поддерживает Java.
</APPLET>
```

Типы `INPUT` в 3.2: TEXT, PASSWORD, CHECKBOX, RADIO, SUBMIT, RESET, FILE, HIDDEN, IMAGE. Валидации, `<LABEL>`, `<BUTTON>`, типов email/date не было; формы обрабатывали CGI-скрипты.
