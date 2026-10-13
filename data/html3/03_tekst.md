# HTML 3.2: разметка текста

```html
<H2 ALIGN=CENTER>Заголовок</H2>
<P>Обычный абзац. <B>жирный</B>, <I>курсив</I>, <U>подчёркнутый</U>, <STRIKE>зачёркнутый</STRIKE>.</P>
<P><BIG>крупнее</BIG> и <SMALL>мельче</SMALL>, H<SUB>2</SUB>O, E=mc<SUP>2</SUP>, <TT>моноширинный</TT>.</P>
<P><EM>акцент</EM>, <STRONG>важное</STRONG>, <CODE>код</CODE>, <KBD>ввод</KBD>, <VAR>переменная</VAR>, <CITE>источник</CITE>, <DFN>определение</DFN>, <SAMP>пример вывода</SAMP>.</P>
<PRE>
Отформатированный   текст
  сохраняет пробелы
</PRE>
<BLOCKQUOTE>Длинная цитата</BLOCKQUOTE>
<ADDRESS>Автор: webmaster@example.com</ADDRESS>
<P>Строка<BR CLEAR=ALL>новая строка ниже картинок</P>
```

- `<BR CLEAR=LEFT|RIGHT|ALL>` переносит строку ниже обтекаемых изображений.
- Закрывающий `</P>` был необязательным.
- `<U>` и `<STRIKE>` в HTML 4 стали устаревшими, в HTML5 вместо них — CSS и `<s>`.
