# HTML 3.2: таблицы

```html
<TABLE BORDER=1 CELLPADDING=4 CELLSPACING=0 WIDTH="100%" ALIGN=CENTER>
<CAPTION ALIGN=TOP>Прайс-лист</CAPTION>
<TR ALIGN=CENTER VALIGN=MIDDLE>
  <TH>Товар</TH><TH>Цена</TH>
</TR>
<TR>
  <TD NOWRAP>Модем 33.6</TD><TD ALIGN=RIGHT>$99</TD>
</TR>
<TR>
  <TD COLSPAN=2 ALIGN=CENTER>Доставка бесплатно</TD>
</TR>
</TABLE>
```

Атрибуты по спецификации HTML 3.2:
- `<TABLE>`: `BORDER`, `CELLPADDING`, `CELLSPACING`, `WIDTH`, `ALIGN`;
- `<TR>`: `ALIGN`, `VALIGN`;
- `<TH>`, `<TD>`: `ROWSPAN`, `COLSPAN`, `NOWRAP`, `ALIGN`, `VALIGN`, `WIDTH`, `HEIGHT`.

`BGCOLOR` у ячеек поддерживали браузеры, но в спецификацию 3.2 он не входил (появился в HTML 4.0 Transitional). В конце 90-х таблицы массово использовали для **раскладки страниц** — сегодня так делать нельзя, нужен CSS.
