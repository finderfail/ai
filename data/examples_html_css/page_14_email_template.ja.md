# HTML/CSS の例: HTML メール

メールクライアント向けの表組みとインラインスタイル。

```html
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f4f4f5">
<tr><td align="center" style="padding:24px">
<table role="presentation" width="600" style="max-width:600px;background:#ffffff;border-radius:12px">
<tr><td style="padding:32px;font-family:Arial,sans-serif;color:#111">
<h1 style="margin:0 0 12px;font-size:22px">Welcome!</h1>
<p style="margin:0 0 20px;line-height:1.5">Thanks for signing up.</p>
<a href="https://example.com" style="background:#4f46e5;color:#fff;padding:12px 20px;border-radius:8px;text-decoration:none">Get started</a>
</td></tr></table></td></tr></table>
```

```css
@media (max-width: 620px) { table[width="600"] { width: 100% !important; } }
```
