# HTML5：リンクと画像

```html
<a href="/about">会社概要</a>
<a href="https://example.com" target="_blank" rel="noopener noreferrer">外部リンク</a>
<a href="mailto:info@example.com">メールする</a>
<a href="tel:+81312345678">電話する</a>
<a href="/file.pdf" download>PDF をダウンロード</a>
<a href="#contacts">連絡先へ</a>

<img src="photo.jpg" alt="写真の説明" width="800" height="600" loading="lazy" decoding="async">

<img src="small.jpg"
     srcset="small.jpg 480w, medium.jpg 960w, large.jpg 1600w"
     sizes="(max-width: 600px) 100vw, 50vw"
     alt="風景">

<picture>
  <source srcset="photo.avif" type="image/avif">
  <source srcset="photo.webp" type="image/webp">
  <img src="photo.jpg" alt="風景">
</picture>
```

- `alt` は必須。装飾的な画像は `alt=""`。
- `width`/`height` は読み込み時のレイアウトのずれを防ぐ。
- `loading="lazy"` は画面外の画像の読み込みを遅らせる。
