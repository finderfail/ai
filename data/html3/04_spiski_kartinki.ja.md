# HTML 3.2：リスト、画像、イメージマップ

```html
<UL TYPE=SQUARE><LI>項目</UL>                     <!-- DISC | CIRCLE | SQUARE -->
<OL TYPE=I START=4><LI>4番目<LI VALUE=10>10番目</OL>   <!-- 1 | a | A | i | I -->
<DL><DT>用語<DD>説明</DL>
<DIR><LI>短いリスト</DIR>  <MENU><LI>メニュー</MENU>

<IMG SRC="logo.gif" ALT="ロゴ" WIDTH=120 HEIGHT=60 BORDER=0
     ALIGN=LEFT HSPACE=10 VSPACE=5>

<IMG SRC="map.gif" USEMAP="#nav" ALT="ナビゲーション" BORDER=0>
<MAP NAME="nav">
  <AREA SHAPE=RECT COORDS="0,0,100,40" HREF="index.html" ALT="ホーム">
  <AREA SHAPE=CIRCLE COORDS="150,20,20" HREF="mail.html" ALT="メール">
</MAP>
```

- `<IMG>` の `ALIGN=LEFT|RIGHT` はテキストの回り込み、`TOP|MIDDLE|BOTTOM` は行内の配置。
- `BORDER=0` でリンク画像の枠を消した。
- クライアントサイドのイメージマップ（`<MAP>`）は HTML 3.2 の新機能。以前はサーバーサイド（`ISMAP`）を使った。
- 閉じタグ `</LI>`、`</DT>`、`</DD>` は省略可能。
