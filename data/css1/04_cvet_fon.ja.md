# CSS1：色と背景

```css
BODY {
  color: black;
  background-color: white;
  background-image: url(paper.gif);
  background-repeat: repeat-y;        /* repeat | repeat-x | repeat-y | no-repeat */
  background-attachment: fixed;       /* scroll | fixed */
  background-position: top center;    /* キーワード、%、長さ */
}
H1 { background: #CCCCFF url(logo.gif) no-repeat }   /* 省略形 */
```

**CSS1 の色：**
- 16の色名：aqua、black、blue、fuchsia、gray、green、lime、maroon、navy、olive、purple、red、silver、teal、white、yellow；
- `#RGB` と `#RRGGBB`：`#F00`、`#FF0000`；
- `rgb(255, 0, 0)` と `rgb(100%, 0%, 0%)`。

透明度（`rgba`、`opacity`）、グラデーション、複数の背景は CSS1 にはない。
