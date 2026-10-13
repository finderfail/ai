# HTML 3.2：文書の構造と装飾

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<HTML>
<HEAD>
<TITLE>私のホームページ</TITLE>
<META NAME="keywords" CONTENT="html, 1997">
</HEAD>
<BODY BGCOLOR="#FFFFFF" TEXT="#000000" LINK="#0000FF" VLINK="#800080" ALINK="#FF0000" BACKGROUND="bg.gif">
<BASEFONT SIZE=3>
<CENTER><H1>ようこそ！</H1></CENTER>
<P ALIGN=RIGHT><FONT SIZE="+1" COLOR="#990000" FACE="Arial">更新日：1997年10月12日</FONT></P>
<HR ALIGN=CENTER WIDTH="80%" SIZE=2 NOSHADE>
<DIV ALIGN=CENTER>中央寄せの文章</DIV>
</BODY>
</HTML>
```

- 装飾は **属性**（`BGCOLOR`、`ALIGN`）と `<FONT>`、`<CENTER>`、`<BASEFONT>` タグで指定した。CSS はまだほとんど対応していなかった。
- `<FONT SIZE>` は 1〜7、または相対値（`+1`、`-2`）。
- `<FONT>` の `FACE` 属性はブラウザが対応していたが、3.2 の仕様にはなかった。
