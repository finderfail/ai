# HTML 3.2：テキストのマークアップ

```html
<H2 ALIGN=CENTER>見出し</H2>
<P>普通の段落。<B>太字</B>、<I>斜体</I>、<U>下線</U>、<STRIKE>取り消し線</STRIKE>。</P>
<P><BIG>大きめ</BIG>と<SMALL>小さめ</SMALL>、H<SUB>2</SUB>O、E=mc<SUP>2</SUP>、<TT>等幅</TT>。</P>
<P><EM>強調</EM>、<STRONG>重要</STRONG>、<CODE>コード</CODE>、<KBD>入力</KBD>、<VAR>変数</VAR>、<CITE>出典</CITE>、<DFN>定義</DFN>、<SAMP>出力例</SAMP>。</P>
<PRE>
整形済み   テキスト
  空白が保たれる
</PRE>
<BLOCKQUOTE>長い引用</BLOCKQUOTE>
<ADDRESS>作成者：webmaster@example.com</ADDRESS>
<P>行<BR CLEAR=ALL>画像の下に新しい行</P>
```

- `<BR CLEAR=LEFT|RIGHT|ALL>` は回り込み画像の下へ改行する。
- 閉じタグ `</P>` は省略可能だった。
- `<U>` と `<STRIKE>` は HTML 4 で非推奨になり、HTML5 では CSS と `<s>` を使う。
