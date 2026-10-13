# HTML 3.2: структура документа и оформление

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<HTML>
<HEAD>
<TITLE>Моя домашняя страница</TITLE>
<META NAME="keywords" CONTENT="html, 1997">
</HEAD>
<BODY BGCOLOR="#FFFFFF" TEXT="#000000" LINK="#0000FF" VLINK="#800080" ALINK="#FF0000" BACKGROUND="bg.gif">
<BASEFONT SIZE=3>
<CENTER><H1>Добро пожаловать!</H1></CENTER>
<P ALIGN=RIGHT><FONT SIZE="+1" COLOR="#990000" FACE="Arial">Обновлено: 12.10.1997</FONT></P>
<HR ALIGN=CENTER WIDTH="80%" SIZE=2 NOSHADE>
<DIV ALIGN=CENTER>Текст по центру</DIV>
</BODY>
</HTML>
```

- Оформление задаётся **атрибутами** (`BGCOLOR`, `ALIGN`) и тегами `<FONT>`, `<CENTER>`, `<BASEFONT>` — CSS ещё почти не поддерживался.
- `<FONT SIZE>` — от 1 до 7 или относительно (`+1`, `-2`).
- Атрибут `FACE` у `<FONT>` поддерживали браузеры, хотя в спецификации 3.2 его не было.
