# HTML 3.2: списки, изображения, карты

```html
<UL TYPE=SQUARE><LI>пункт</UL>                     <!-- DISC | CIRCLE | SQUARE -->
<OL TYPE=I START=4><LI>четвёртый<LI VALUE=10>десятый</OL>   <!-- 1 | a | A | i | I -->
<DL><DT>Термин<DD>Определение</DL>
<DIR><LI>короткий список</DIR>  <MENU><LI>меню</MENU>

<IMG SRC="logo.gif" ALT="Логотип" WIDTH=120 HEIGHT=60 BORDER=0
     ALIGN=LEFT HSPACE=10 VSPACE=5>

<IMG SRC="map.gif" USEMAP="#nav" ALT="Навигация" BORDER=0>
<MAP NAME="nav">
  <AREA SHAPE=RECT COORDS="0,0,100,40" HREF="index.html" ALT="Главная">
  <AREA SHAPE=CIRCLE COORDS="150,20,20" HREF="mail.html" ALT="Почта">
</MAP>
```

- `ALIGN=LEFT|RIGHT` у `<IMG>` включает обтекание текстом; `TOP|MIDDLE|BOTTOM` — выравнивание в строке.
- `BORDER=0` убирал рамку у картинки-ссылки.
- Клиентские карты изображений (`<MAP>`) — нововведение HTML 3.2; раньше использовали серверные (`ISMAP`).
- Закрывающие `</LI>`, `</DT>`, `</DD>` необязательны.
