# HTML 3.2：表

```html
<TABLE BORDER=1 CELLPADDING=4 CELLSPACING=0 WIDTH="100%" ALIGN=CENTER>
<CAPTION ALIGN=TOP>価格表</CAPTION>
<TR ALIGN=CENTER VALIGN=MIDDLE>
  <TH>商品</TH><TH>価格</TH>
</TR>
<TR>
  <TD NOWRAP>モデム 33.6</TD><TD ALIGN=RIGHT>$99</TD>
</TR>
<TR>
  <TD COLSPAN=2 ALIGN=CENTER>送料無料</TD>
</TR>
</TABLE>
```

HTML 3.2 の仕様上の属性：
- `<TABLE>`：`BORDER`、`CELLPADDING`、`CELLSPACING`、`WIDTH`、`ALIGN`；
- `<TR>`：`ALIGN`、`VALIGN`；
- `<TH>`、`<TD>`：`ROWSPAN`、`COLSPAN`、`NOWRAP`、`ALIGN`、`VALIGN`、`WIDTH`、`HEIGHT`。

セルの `BGCOLOR` はブラウザが対応していたが、3.2 の仕様には含まれていなかった（HTML 4.0 Transitional で追加）。1990年代後半は **ページのレイアウト** に表が多用されたが、今は CSS を使うべき。
